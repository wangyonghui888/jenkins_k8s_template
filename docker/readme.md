# 构建并提交镜像
#### python3.6镜像  
1. docker build --tag swc-harbor.nioint.com/sqe/automation_python36:v1 -f Dockerfile_py36 ./
2. docker login https://swc-harbor.nioint.com
3. docker push swc-harbor.nioint.com/sqe/automation_python36:v1

#### java8镜像  
1. docker build --tag swc-harbor.nioint.com/sqe/automation_java8:v2 -f Dockerfile_java8 ./
2. docker login https://swc-harbor.nioint.com
3. docker push swc-harbor.nioint.com/sqe/automation_java8:v2
