# Building docker images

### Build when Dockerfile exists:
```bash
docker image build -t NAME:TAG
```
Flags:
* --rm: remove intermediate containers
* --label: add metadata

### Using stdin:
```bash
docker image build -t NAME:TAG -<<EOF
> FROM centos
> VOLUME ["/sys/fs/cgroup"]
> EOF
```
### Using git:
```bash
docker image build -t image-git https://github.com/dockeruser/folder.git#branch
```

