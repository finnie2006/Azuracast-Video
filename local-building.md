# How to build the image locally for modification

1. Clone the repository
2. Go into the image directory
3. Fix permissions with the following commands:
```shell
chmod +x builder.sh
chmod +x hooks/*
```
4. Then run `./builder.sh latest build` to build the Dockerfile
