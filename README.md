# microservices-scaffold
Barebones Python with Django Microservices

# Docker

Create and push the image

    docker build -t templatedjango -f Dockerfile .

Test the image:

    docker run -d -p 8000:8000 templatedjango
    
    
Push to Kubernetes:

    kubectl create -f service.yaml
    
    
## How to contrib

TODO

### Update docs

   sphinx-build -b html docs/ _build