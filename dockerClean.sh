set -o errexit

docker stop web_grupo4
docker system prune -f
docker ps -a
