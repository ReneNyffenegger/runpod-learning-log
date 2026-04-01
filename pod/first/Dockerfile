# FROM alpine:latest

# Use minimal Docker image with glibc (not with musl) so that nvidia-smi is able to run.
FROM greyfoxit/alpine-glibc

# Install OpenSSH server
RUN apk add --no-cache openssh

# Generate host keys and set up basic config
RUN ssh-keygen -A

# Allow root login with password (for simplicity)
RUN echo 'root:thePassw0rd' | chpasswd

RUN sed -i 's/#PermitRootLogin.*/PermitRootLogin yes/'               /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config

RUN echo nvidia-smi > /root/.profile

# Create required runtime directory
RUN mkdir -p /var/run/sshd

#
# Start ssh daemon
#   -D  sshd will not become a daemon (does not detach)
#   -e  write debug logs to stderr rather than to the system log
#
CMD ["/usr/sbin/sshd", "-D", "-e"]
