Write a kubernetes (preferably helm) template that deploys nginx with custom configuration and exposes services as NodePort -

followed below commands, to setup helm and nginx.

------------------------------------------------------------------------------------------------------------
wget https://get.helm.sh/helm-v3.5.0-linux-amd64.tar.gz
tar -xzf helm-v3.5.0-linux-amd64.tar.gz
mv ./linux-amd64/helm /usr/local/bin/
ls -l /usr/local/bin/
helm version
helm create helloworld
ll
tree helloworld/
helm repo add stable https://charts.helm.sh/stable
helm install myfirstchart helloworld
helm list -a
kubectl get all
vi helloworld/values.yaml
helm inspect values helloworld/
helm inspect chart helloworld/
kubectl get all
helm list -a
helm upgrade myfirstchart helloworld
helm list -a
kubectl get all
-> validate by UI --- DONE
helm history myfirstchart
