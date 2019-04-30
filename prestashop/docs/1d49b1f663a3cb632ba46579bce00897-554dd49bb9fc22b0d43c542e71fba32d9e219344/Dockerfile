FROM prestashop/prestashop:1.7-7.0

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget tar

# Install modules
COPY add_module.sh module_dependencies.txt /tmp/
# Docker image has some issues with line endings when developing it on Windows, within empty line added we ensure those are correct 
RUN echo '' >> /tmp/module_deps.txt
RUN chmod +x /tmp/add_modules.sh
RUN /tmp/add_modules.sh /tmp/module_deps.txt
RUN rm -rf /tmp/add_modules.sh /tmp/module_deps.txt

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*