minikube start --driver=docker
kubectl create deployment myapp --image=nginx
kubectl expose deployment myapp --port=80 --type=NodePort
kubectl scale deployment myapp --replicas=3
kubectl get all
minikube service myapp
kubectl delete deployment myapp
kubectl delete service myapp