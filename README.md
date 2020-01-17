# coding_challenge
Coding Challenge for DeepVisionAI<br/>
Requires:<br/>
 python 3.6<br/>
 flask<br/>
 connexion<br/>
 connexion[swagger-ui]<br/>
 pytest<br/>
<br/>
Unit Deploy:<br/>
 docker build -t coding_challenge_docker:latest .<br/>
 <br/>
Unit Run:<br/>
 docker run -d -p 5000:5000 coding_challenge_docker:latest<br/>
<br/>
Usage:<br/>
 -Open WebBrowser and go to: http://localhost:5000/api/efemerides?day={AAAA-MM-DD}<br/>
