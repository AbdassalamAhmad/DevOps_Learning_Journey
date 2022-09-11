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
        - Cluster gateway to clients. (clients talk to cluster through API server.)
        - Gets the commands of update or query from the cluster.
        - Runs Authentication.
    2. Scheduler:
        - Gets Instructions from API server and decide intelligently on which node to perform it. [29:40]
        - Kubelet is the one who perform the instruction.
    3. Controller Manager:
        - Detect cluster state changes: like crashing some pod.
        - Sends request to Scheduler when pod die to recreate it.
    4. etcd: 

