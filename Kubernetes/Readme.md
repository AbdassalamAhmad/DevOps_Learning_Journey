# Kubernetes Resources

- I've used **Kubernetes Tutorial for Beginners** [**a YouTube course**](https://www.youtube.com/watch?v=X48VuDVv0do) from 'TechWorld with Nana' YouTube channel BY [Nana Janashia](https://www.linkedin.com/in/nana-janashia/).
- I've used this [**KodeKloud Tutorial**](https://www.youtube.com/watch?v=kJscDZfHXrQ) to learn about Helm commands.
- I've used this [**Helm Docs**](https://helm.sh/docs/howto/charts_tips_and_tricks/) to learn more about Helm commands.

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
    - It's like deployments, but Used for replicating stateful apps like database.
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
        - Gets Instructions (deploying a new pod) from API server and decide intelligently on which node to perform it. [29:40]
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
$ minikube dashboard # start a dashboard with info about pods and deployments AND a lot more.

$ minikube start # Start a cluster, and if you don't have kubernetes installed it will install it.
$ minikube stop/delete # Stop/delete a cluster.
$ minikube status # Display status of api, kubelet and kubeconfig.

$ minikube load image mongo:6.0.1 # IMPORTANT: when applying deployment, it fail without using this command due to high size.
$ minikube service <servicename> # to make a service have external IP address.
$ minikube addons enable ingress
$ minikube tunnel # your ingress resources would be available at "127.0.0.1"
```
**Get information / Describe Commands:**
```bash
$ kubectl get nodes # Display all of the nodes, for minikube only one node (master and worker in one node).
$ kubectl get pods -o wide # Display all of the working pods and in wide to see its IP address.
$ kubectl get services # Display services.
$ kubectl get replicaset # Display all replicaset.
$ kubectl get deployment # Display all deployments.
$ kubectl get secrets # Display all secrets.
$ kubectl get namespace # Display all namespaces.
$ kubectl get ingress # Display all Ingress.

$ kubectl describe pods <podname> # Gives more info about a pod or number of pods.
$ kubectl describe deployment <deploymentname> # Gives more info about a deployment or number of deployments.
$ kubectl describe service <servicename> # Gives info about the service like IP address of pod and ports.
```

**Create Commands:**
```bash
$ kubectl apply -f <filename.yaml> # Create a deployment from filename.yaml file.
$ kubectl delete -f nginx.yaml # Delete the deployment of nginx.yaml file.

$ kubectl create namespace <name> # create a namespace
$ kubectl create deployment <name> --image:image-name #  Create a deployment based on image specified from docker hub.
$ kubectl delete deployment <deploymentname> # Delete the deployment and all of its compnents like pods.
$ kubectl edit deployment nginx-depl # Edit configuration of the deployment like image, replicasets or resource limits.

$ kubectl rollout restart deploymnet <deploymnet-name>  # restart all pods of that deploymnet.
```
**Debugging Commands:**
```bash
$ kubectl logs <podname> # Shows the Logs of the container in pod.
$ kubectl exec -it nginx-depl-1-696c55898f-2hknw -- sh
$ # This command will enter us into the nginx container shell.

$ kubectl top node/pod # Returns current CPU and memory usage for a cluster’s pods or nodes
```

## Namespaces:
### Benefits of Using Namespaces:
1. Resources grouped together in namespaces: 
    - Databases-namespace.
    - Monitoring-namespace.
    - Logging-namespace.
    - Main-Application-namespace.
2. Resolving conflicts from many teams:
    - Putting every team in a namespace to avoid overwriting.
3. Resources Sharing:
    - You don't have to install same app on two different cluster.
    - Install it on same cluster with two different namespaces.
    - Blue/Green Deployment.
4. Resources and access limits for different teams:
    - Team 1 can't remove files from team 2.
    - team 1 can't use more ram than limit to not interrupt team 1.

### Sharing Resources Rules:
- ConfigMaps and Secrets can't be shared through different namespaces.
- Services can be shared through different namespaces.
- Columes and nodes can't live in namesspaces.

### How to Create Namespace:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: mongodb-configmap
  namespace: my-namespace # Here we Create a namespace and assign this ConfigMap to it.
data:
  database_url: mongodb-service.database # .database refer to a namespace called database 
```
- How to get resources of a namespace?
1. $ kubectl get all -n my-namespace
2. install kubectx and then use kubens from [here](https://github.com/ahmetb/kubectx#installation).

## Ingress:
Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. <br>
Traffic routing is controlled by rules defined on the Ingress resource.
### Ingress Controller:
- Evaluate all of the rules in ingress yaml file.
- Manages network redirections.
- It is Entrypoint to the cluster.
- I've used K8s Inginx Ingress Controller.
- You need to have LoadBalancer before Ingress Controller [02:10:12].
- Installation : $ minikube addons enable ingress
- You can configure default error message [02:19:13].
- You can add multiple paths and map it to different services [02:20:23].
- You can add security to your url to begin with https [02:22:40].
- NOTE: I've a problem in running it on windows 10.

## Helm:
### Helm Charts:
- It's like Docker Hub that has docker containers for specific apps.
- It has Bundle of YAML files for different softwares like database or monitoring or logging apps.
- You can create your own helm charts with Helm.
- You can pull others helm charts.
- You don't have to run multiple "$ kubectl apply -f" commands.
- You can delete all of the kubernetes cluster components with one command (uninstall).
```bash
$ helm create mongo-chart # create a dir named mongo-chart with all files for you to edit.
$ helm install <chartname> <folderpath> # Install all of the components into kubernetes cluster.
$ helm upgrade <chartname> <foldername> # Upgrade new valuse into the cluster.
$ helm rollback <chartname> <REVISION> # rollback to a specific previous version.
$ helm history <chartname> # See revision numbers.
$ helm get manifest <chartname> # Display all yaml files in the current version.
$ helm uninstall <chartname> # Uninstall all the components of the cluster.
$ helm search hub wordpress # search for wordpress charts in the hub.
```

## Volumes:
- There are three components : PV, PVC, SC. (Presistant Volume, Presistant Volume Claim, Source Control )
- PVC asks for volume storage from SC.
- SC has internal and external provisioner to get the requested storage.
- PV gets created by SC with the required storage.
