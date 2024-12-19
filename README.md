## Docker란?
- 컨테이너를 사용해 애플리케이션을 신속하게 구축, 테스트 및 배포할 수 있는 소프트웨어 플랫폼입니다.
- VM과 다르게 필요한 기능만 가져다 쓰기 때문에 가볍고 효율적입니다.
### Docker 구성요소
- 출처 : https://docs.docker.com/get-started/docker-overview/#docker-architecture image
  ![image](https://github.com/user-attachments/assets/74b3771f-3115-4c00-aedf-796e553e6e6a)

### Docker daemon (dockerd) : 도커 엔진
- Docker API의 요청에 따라 이미지, 컨테이너, 네트워크, 볼륨과 같은 도커 객체를 관리합니다. 다른 데몬과 통신하여 도커 서비스를 관리할 수도 있습니다.
### Docker client
- docker run과 같은 명령어를 사용할 때, 클라이언트는 이러한 명령어를 dockerd로 보내 실행합니다. 도커 명령어는 도커 API를 사용합니다. 도커 클라이언트는 여러 데몬과 통신할 수 있습니다.
### Docker Host
- 도커가 띄워져있는 서버입니다. 컨테이너와 이미지를 관리합니다.
### Docker Desktop
- Mac, Windows 또는 Linux 환경에 설치하기 쉬운 애플리케이션으로, 컨테이너형 애플리케이션과 마이크로서비스를 구축하고 공유할 수 있습니다. 도커 데몬(dockerd), 도커 클라이언트(docker), Docker Compose, Docker Content Trust, Kubernetes, Credential Helper가 포함됩니다.
### Docker registires
- Docker Images를 저장합니다. Docker hub는 누구나 사용할 수 있는 공용 레지스트리이며, Docker는 기본적으로 Docker hub에서 이미지를 찾습니다. 개인 레지스트리를 실행할 수도 있습니다.
- docker pull 또는 docker run 명령을 사용하면 Docker는 구성된 레지스트리에서 필요한 이미지를 가져옵니다. docker push 명령을 사용하면 Docker는 Image를 구성된 레지스트리로 push합니다.
  
## Docker objects
Docker를 사용할 때는 이미지, 컨테이너, 네트워크, 볼륨, 플러그인 및 기타 객체를 생성하고 사용하는 것입니다. 이 섹션에서는 이러한 객체 중 일부에 대한 간략한 개요를 설명합니다.

### Images
- Docker container를 만드는 지침이 포함된 읽기 전용 template입니다. 종종 이미지는 다른 이미지를 기반으로 하며, 추가적인 사용자 정의가 필요합니다.
- 예를 들어, ubuntu이미지를 기반으로 하지만 Apache 웹 서버와 애플리케이션을 설치하고 애플리케이션을 실행하는 데 필요한 구성 세부 정보를 포함한 이미지를 만들 수 있습니다.
- 자신만의 이미지를 만들 수도 있고 다른 사람이 만들어 레지스트리에 게시한 이미지만 사용할 수도 있습니다. 자신의 이미지를 빌드하려면 이미지를 생성하고 실행하는 데 필요한 단계를 정의하는 간단한 구문을 가진 Dockerfile을 만들어야 합니다.
- Dockerfile의 각 명령어는 이미지에 layers를 생성합니다. Dockerfile을 변경하고 이미지를 재구성할 때 변경된 레이어만 재구성됩니다. 이는 다른 가상화 기술에 비해 이미지가 가볍고 작고 빠른 이유 중 하나입니다.
### Containers
- 이미지의 실행 가능한 인스턴스입니다. Docker API 또는 CLI를 사용하여 컨테이너를 생성/실행/중지/이동/삭제할 수 있습니다. 컨테이너를 하나 이상의 네트워크에 연결하거나, 스토리지를 연결하거나, 현재 상태를 기반으로 새 이미지를 생성할 수도 있습니다.
- 컨테이너는 이미지에 의해 정의되며, 기본적으로 컨테이너는 다른 컨테이너 및 호스트 컴퓨터와 비교적 잘 격리되어 있습니다. 따라서 특정 컨테이너에서 수정사항이 생겨도 다른 컨테이너와 호스트는 변경 사항이 없습니다.
- 컨테이너는 이미지를 읽기 전용으로 사용하되, 이미지에서 변경된 사항만 컨테이너 계층에 저장하기 때문에 컨테이너에서 무엇을 해도 이미지는 영향을 받지 않습니다.