set -o errexit

docker build -t app_grupo4 .
docker create --name web_grupo4 -p 8000:8000 -v /home/marco/docker_vols/:/data app_grupo4
docker start web_grupo4
docker exec -it web_grupo4 bash
