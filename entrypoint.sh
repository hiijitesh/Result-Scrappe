date=$(date +%Y.%m.%d)
echo "Date"  $date
echo "checkout to dev"
git checkout dev
echo "Version: " $date
echo "Docker Build Started"
docker build -t hiijitesh/result-bot-1:$date .
echo "Docker Build complete"
echo "Pushing image to Dockerhub"
docker push hiijitesh/result-bot-1:$date
echo "Docker Push complete"
docker-compose down && docker-compose up -d