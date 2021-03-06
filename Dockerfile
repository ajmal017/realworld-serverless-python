FROM lambci/lambda-base:build

ENV PATH=/var/lang/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib \
    AWS_EXECUTION_ENV=AWS_Lambda_python3.6 \
    PYTHONPATH=/var/runtime \
    NODE_PATH=/var/runtime:/var/task:/var/runtime/node_modules \
    npm_config_unsafe-perm=true \
    PKG_CONFIG_PATH=/var/lang/lib/pkgconfig:/usr/lib64/pkgconfig:/usr/share/pkgconfig

RUN rm -rf /var/runtime /var/lang

RUN curl https://lambci.s3.amazonaws.com/fs/python3.6.tgz | tar -xz -C / && \
  sed -i '/^prefix=/c\prefix=/var/lang' /var/lang/lib/pkgconfig/python-3.6.pc && \
  curl https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz | tar -xJ && \
  cd Python-3.6.1 && \
  LIBS="$LIBS -lutil -lrt" ./configure --prefix=/var/lang && \
  make -j$(getconf _NPROCESSORS_ONLN) libinstall inclinstall && \
  cd .. && \
  rm -rf Python-3.6.1 && \
  pip3 install -U pip awscli virtualenv --no-cache-dir

RUN curl https://lambci.s3.amazonaws.com/fs/nodejs8.10.tgz | tar -zx -C /

ADD . /realworld

WORKDIR /realworld

RUN npm install -g npx

RUN pip3 install -r requirements.txt
RUN npm install
