FROM fedora

RUN    dnf -y --setopt=tsflags=nodocs --setopt=install_weak_deps=False upgrade \
    && dnf -y --setopt=tsflags=nodocs --setopt=install_weak_deps=False install \
            selenium \
            selenium-manager \
            firefox \
            python-unversioned-command \
    && dnf clean all \
    && useradd -m batedor

USER batedor
WORKDIR /home/batedor

ADD .



# Incompleto...

CMD ["/bin/bash"]
