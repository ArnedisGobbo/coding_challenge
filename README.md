# coding_challenge
Coding Challenge for DeepVisionAI
Requires:
 python 3.6
 flask
 connexion
 connexion[swagger-ui]
 pytest

Unit Deploy:
 docker build -t coding_challenge_docker:latest .
 
Unit Run:
 docker run -d -p 5000:5000 coding_challenge_docker:latest

Usage:
 -Open WebBrowser and go to: http://localhost:5000/api/efemerides?day={AAAA-MM-DD}
