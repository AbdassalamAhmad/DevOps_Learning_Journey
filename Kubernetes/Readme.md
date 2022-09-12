# Kubernetes Resources

- I've used **Kubernetes Tutorial for Beginners** [**a YouTube course**](https://www.youtube.com/watch?v=X48VuDVv0do) from 'TechWorld with Nana' YouTube channel BY [Nana Janashia](https://www.linkedin.com/in/nana-janashia/).

## Kubernetes Components:
- **Pods, Replicas, and Deployments**: 
    - Deployments are blueprint for creating pods.
    - Replicas are number of copies of pods to ensure NoDownTime.
    - Pod is the smallest unit in k8s.
    - It has usually one container.

- **Services**:
    - There are many types; most used one is LoadBalancer.
    - It's like a permenant IP that connects pods together.

- **Ingress**:
    - Forwards external requests to LoadBalancer (service).
    - Change the url from ip:port to regular URL.

- **ConfigMaps**:
    - It's external configuration for the application.

- **SecretMap**:
    - Same as ConfigMaps but for sensetive data.
    - Uses base64 encoding system to secure the sensetive data like usernames and passwords.

- **Volumes**:
    - Used for data persistence.
    - You can store data on local machine or remote like AWS.

- **StatefulSet**:
    - Used for replicating stateful apps like database.
    - It's hard not like replicas.
    - Usually are databases stored outside of K8s cluster like on cloud.

## Kubernetes Architecture: 
- **Worker Nodes:**
    1. Kubelet: 
        - Assign resources to the Node.
        - Interacts with the container runtime (like pods do with container).
    2. Kube Proxy: Forwards the request intelligently to a specific pod.
    3. Container Runtime: Like Docker, that manages containers.

- **Master Node:**
    1. API Server: 
        - Cluster gateway to clients. (clients talk to cluster through API server using UI dashbaord, API OR kubectl.)
        - Gets the commands of update or query from the cluster.
        - Runs Authentication.
    2. Scheduler:
        - Gets Instructions from API server and decide intelligently on which node to perform it. [29:40]
        - Kubelet is the one who perform the instruction.
    3. Controller Manager:
        - Detect cluster state changes: like crashing some pod.
        - Sends request to Scheduler when pod die to recreate it.
    4. etcd: 
        - Cluster changes and data are stored in etcd.
        - Data like how many pods and state and helth of the pods are stored in it.

- **Minikube**: 
    - Minikube create a virtual machine on your laptop to start a node server.
    - Master and Node processes runs on the same node server to solve resources problem.

## Commands I've learned:
**minikube commadns:**
```bash
$ minikube start # Start a cluster, and if you don't have kubernetes installed it will install it.
$ minikube dashboard # start a dashboard with info about pods and deployments AND a lot more.
$ minikube stop/delete # Stop/delete a cluster.
$ minikube status # Display status of api, kubelet and kubeconfig.

```
**Get information / Describe Commands:**
```bash
$ kubectl get nodes # Display all of the nodes, for minikube only one node (master and worker in one node).
$ kubectl get pods # Display all of the working pods.
$ kubectl get services # Display services.
$ kubectl get replicaset # Display all replicaset.
$ kubectl get deployment # Display all deployments.
$ kubectl describe pods <podname> # Gives more info about a pod or number of pods.
$ kubectl describe deployment <deploymentname> # Gives more info about a deployment or number of deployments.
```

**Create Commands:**
```bash
$ kubectl apply -f <filename.yaml> # Create a deployment from filename.yaml file.
$ kubectl create deployment <name> --image:image-name #  Create a deployment based on image specified from docker hub.
$ kubectl edit deployment nginx-depl # Edit configuration of the deployment like image, replicasets or resource limits.
$ kubectl delete deployment <deploymentname> # Delete the deployment and all of its compnents like pods.
$ kubectl delete -f nginx.yaml # Delete the deployment of nginx.yaml file.
$ kubectl rollout restart deploymnet <deploymnet-name>  # restart all pods of that deploymnet.
```
**Debugging Commands:**
```bash
$ kubectl logs <podname> # Shows the Logs of the container in pod.
$ kubectl exec -it nginx-depl-1-696c55898f-2hknw -- sh
$ # This command will enter us into the nginx container shell.

$ kubectl top node/pod # Returns current CPU and memory usage for a cluster’s pods or nodes
```

