Introduction
------------------------------

The cdf2cim micro web-service is a python application augmented by several shell commands.

Installing
------------------------------

**Step 1: Download source code from GitHub**

```
cd YOUR_WORKING_DIRECTORY
git clone https://github.com/ES-DOC/esdoc-cd2cim-ws.git
```

**Step 2: Run installer**

```
source YOUR_WORKING_DIRECTORY/esdoc-cd2cim-ws/sh/activate && cdf2cim-ws-install
```

This installs configuration files and a virtual environment into the ops folder.

**Step 3: Review installation**

Explore the install directory, i.e. YOUR_WORKING_DIRECTORY/esdoc-cd2cim-ws.  The ops sub-directory contains local resources created during the lifetime of the shell, this includes config files, logs, daemons, and a virtual environment.

**Step 4: Security**

The web-service applies a security policy whereby each request is authenticated and authorized against the GitHub API.  If you wish to run/test this policy usage then you will need to obtain a GitHub access token from the ES-DOC team.  Once you have the token you must set the following environment variable: CDF2CIM_WS_GITHUB_ACCESS_TOKEN.  You will also need to update your ws.conf: apply_security_policy = true.
