## Example: Httpbin

This example demonstrates a basic deployment configuration that supports a local instance of httpbin running under a configuration that could be used for a production deployment as well.  

The deployment files are in the directory `httpbin`  

In particular, note that httpbin-virtual-service definition is the same for both tls and non-tls. It is the gateway definition that changes to incorporate external TLS access.  

**First**, create a localhost entry for `local.httpbin.org` that resolves to the istio-ingressgateway EXTERNAL-IP:  

```bash
$ kubectl get svc istio-ingressgateway -n istio-system  # get the IP for the istio-ingressgateway
$ sudo hostess add local.httpbin.org EXTERNAL-IP        # create a local entry, requires admin password
```

**deploy httpbin without tls**:  

```bash
$ inv httpbin.deploy
```

From your browser you can now go to `http://local.httpbin.org` to access the locally running httpbin service without tls.  

**deploy httpbin with tls**  

```bash
$ inv httpbin.deploy -tls
```

The deploy will generate the necessary certificates for `local.httpbin.org` using the local Root CA and deploy these to istio-system on minikube.

You can now use `https://local.httpbin.org/`    

Use curl to display header and certificate validation info  
```bash
$ curl -v -HHost:local.httpbin.org --cacert local.httpbin.org.crt "https://local.httpbin.org/status/418"
```

You should see something like the following: (the IPs will match what you used to create the local DNS entry)
```bash
*   Trying 10.105.19.134...
* TCP_NODELAY set
* Connected to local.httpbin.org (10.105.19.134) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: local.httpbin.org.crt
  CApath: none
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-CHACHA20-POLY1305
* ALPN, server accepted to use h2
* Server certificate:
*  subject: O=mkcert development certificate; OU=<your local device information>
*  start date: Jun  1 00:00:00 2019 GMT
*  expire date: Dec 29 19:25:26 2030 GMT
*  subjectAltName: host "local.httpbin.org" matched cert's "local.httpbin.org"
*  issuer: O=mkcert development CA; OU=n<your local device information>; CN=mkcert <your local device information>
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7f813d80f800)
> GET /status/418 HTTP/2
> Host:local.httpbin.org
> User-Agent: curl/7.64.1
> Accept: */*
>
* Connection state changed (MAX_CONCURRENT_STREAMS == 2147483647)!
< HTTP/2 418
< server: istio-envoy
< date: Tue, 29 Dec 2020 19:27:40 GMT
< x-more-info: http://tools.ietf.org/html/rfc2324
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-length: 135
< x-envoy-upstream-service-time: 32
<

    -=[ teapot ]=-

       _...._
     .'  _ _ `.
    | ."` ^ `". _,
    \_;`"---"`|//
      |       ;/
      \_     _/
        `"""`
* Connection #0 to host local.httpbin.org left intact
* Closing connection 0
```

**clean up**
```bash
$ inv httpbin.rm
$ sudo hostess rm local.httpbin.org
```

[Return](doc/examples.md)