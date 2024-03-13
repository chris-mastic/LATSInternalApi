FLASK_SECRET_KEY DISCUSSIONS AND ADDITIONAL NOTES

A Flask SECRET_KEY is a string of bytes that is used to sign the session cookie and other data that
needs to be encrypted. A flask session is a dictionary-like object that stores data across requests
in a signed cookie. The SECRET_KEY (app.secret_key) must be set before using the session object, otherwise Flask
will raise an error.

The app.secret_key is used to sign the session cookie and other data that needs encrypted. You can 
generate a random secret key using os.random() or other methods. YOu should keep the secret key
consistent and secret across you app instances.

Session cookie:
    A session cookie is a temporary cookie that is stored on your device only during a single visit to
    a website. It is used to remember information such as login credentials, items in a shopping cart,
    or preferences for that website. A session cookie is deleted when you close your browser or end
    the session.

    It is different from a persistent cookie, which is stored on your device for a longer period
    of time and can be used to tracky your behaviour or preferences across multiple website.

    Session cookies are temporary and considered less risky than persistent cookies,as they do
    not store personal data for a long period of time. However, they may still require consent
    under some privacy laws depending on how they are used and what info they store.

    Where do I get SECRET_KEY for Flask? - Stack Overflow  https://stackoverflow.com/questions/34902378/where-do-i-get-secret-key-for-flask
    2: How to Set Up Basic User Authentication in a Flask App - freeCodeCamp.org  https://www.freecodecamp.org/news/how-to-setup-user-authentication-in-flask/
     3: Where should I place the secret key in Flask? - Stack Overflow   https://stackoverflow.com/questions/30873189/where-should-i-place-the-secret-key-in-flask
     4: python - demystify Flask app.secret_key - Stack Overflow  https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key
     5: How do I enforce unique user names in Flask? - Stack Overflow : How to Set Up Basic User Authentication in a Flask App - freeCodeCamp.org
        https://www.freecodecamp.org/news/how-to-setup-user-authentication-in-flask/


# Method 1: Use app.secret_key
app.secret_key = b'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

# Method 2: Use app.config
app.config['SECRET_KEY'] = b'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

# Method 3: Load from a config file
app.config.from_pyfile('config.py') # if your config file's name is config.py

# Method 4: 
# In your terminal, set an environment variable named FLASK_SECRET_KEY
export FLASK_SECRET_KEY=b'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
# Method 5:
# In your app file
app.secret_key = os.environ.get('FLASK_SECRET_KEY') or os.urandom(16)



# Set and get session data
session['username'] = 'Alice'
session['logged_in'] = True
username = session.get('username')
logged_in = session.get('logged_in')


The answer below pertains primarily to Signed Cookies, an implementation of the concept of sessions (as used in web applications). Flask offers both, normal (unsigned) cookies (via request.cookies and response.set_cookie()) and signed cookies (via flask.session). The answer has two parts: the first describes how a Signed Cookie is generated, and the second is presented as a series of Question/Answer that address different aspects of the scheme. The syntax used for the examples is Python3, but the concepts apply also to previous versions.

What is SECRET_KEY (or how to create a Signed Cookie)?
Signing cookies is a preventive measure against cookie tampering. During the process of signing a cookie, the SECRET_KEY is used in a way similar to how a "salt" would be used to muddle a password before hashing it. Here's a (widely) simplified description of the concept. The code in the examples is meant to be illustrative. Many of the steps have been omitted and not all of the functions actually exist. The goal here is to provide a general understanding of the main idea, but practical implementations will likely be a bit more involved. Also, keep in mind that Flask already provides most of this for you in the background. So, besides setting values to your cookie (via the session API) and providing a SECRET_KEY, it's not only ill-advised to re-implement this yourself, but there's no need to do so:

A poor man's cookie signature
Before sending a Response to the browser:
( 1 ) First a SECRET_KEY is established. It should only be known to the application and should be kept relatively constant during the application's life cycle, including through application restarts.

# choose a salt, a secret string of bytes
>>> SECRET_KEY = 'my super secret key'.encode('utf8')
( 2 ) create a cookie

>>> cookie = make_cookie(
...     name='_profile', 
...     content='uid=382|membership=regular',
...     ...
...     expires='July 1 2030...'
... )

>>> print(cookie)
name: _profile
content: uid=382|membership=regular...
    ...
    ...
expires: July 1 2030, 1:20:40 AM UTC
( 3 ) to create a signature, append (or prepend) the SECRET_KEY to the cookie byte string, then generate a hash from that combination.

# encode and salt the cookie, then hash the result
>>> cookie_bytes = str(cookie).encode('utf8')
>>> signature = sha1(cookie_bytes+SECRET_KEY).hexdigest()
>>> print(signature)
7ae0e9e033b5fa53aa....
( 4 ) Now affix the signature at one end of the content field of the original cookie.

# include signature as part of the cookie
>>> cookie.content = cookie.content + '|' + signature
>>> print(cookie)
name: _profile
content: uid=382|membership=regular|7ae0e9...  <--- signature
domain: .example.com
path: /
send for: Encrypted connections only
expires: July 1 2030, 1:20:40 AM UTC
and that's what is sent to the client.

# add cookie to response
>>> response.set_cookie(cookie)
# send to browser --> 
Upon receiving the cookie from the browser:
( 5 ) When the browser returns this cookie back to the server, strip the signature from the cookie's content field to get back the original cookie.

# Upon receiving the cookie from browser
>>> cookie = request.get_cookie()
# pop the signature out of the cookie
>>> (cookie.content, popped_signature) = cookie.content.rsplit('|', 1)
( 6 ) Use the original cookie with the application's SECRET_KEY to recalculate the signature using the same method as in step 3.

# recalculate signature using SECRET_KEY and original cookie
>>> cookie_bytes = str(cookie).encode('utf8')
>>> calculated_signature = sha1(cookie_bytes+SECRET_KEY).hexdigest()
( 7 ) Compare the calculated result with the signature previously popped out of the just received cookie. If they match, we know that the cookie has not been messed with. But if even just a space has been added to the cookie, the signatures won't match.

# if both signatures match, your cookie has not been modified
>>> good_cookie = popped_signature==calculated_signature
( 8 ) If they don't match then you may respond with any number of actions, log the event, discard the cookie, issue a fresh one, redirect to a login page, etc.

>>> if not good_cookie:
...     security_log(cookie)
Hash-based Message Authentication Code (HMAC)
The type of signature generated above that requires a secret key to ensure the integrity of some contents is called in cryptography a Message Authentication Code or MAC.

I specified earlier that the example above is an oversimplification of that concept and that it wasn't a good idea to implement your own signing. That's because the algorithm used to sign cookies in Flask is called HMAC and is a bit more involved than the above simple step-by-step. The general idea is the same, but due to reasons beyond the scope of this discussion, the series of computations are a tad bit more complex. If you're still interested in crafting a DIY, as it's usually the case, Python has some modules to help you get started :) here's a starting block:

import hmac
import hashlib

def create_signature(secret_key, msg, digestmod=None):
    if digestmod is None:
        digestmod = hashlib.sha1
    mac = hmac.new(secret_key, msg=msg, digestmod=digestmod)
    return mac.digest()
The documentation for HMAC and hashlib.

The "Demystification" of SECRET_KEY :)
What's a "signature" in this context?
It's a method to ensure that some content has not been modified by anyone other than a person or an entity authorized to do so.

One of the simplest forms of signature is the "checksum", which simply verifies that two pieces of data are the same. For example, when installing software from source it's important to first confirm that your copy of the source code is identical to the author's. A common approach to do this is to run the source through a cryptographic hash function and compare the output with the checksum published on the project's home page.

Let's say for instance that you're about to download a project's source in a gzipped file from a web mirror. The SHA1 checksum published on the project's web page is 'eb84e8da7ca23e9f83....'

# so you get the code from the mirror
download https://mirror.example-codedump.com/source_code.tar.gz
# you calculate the hash as instructed
sha1(source_code.tar.gz)
> eb84e8da7c....
Both hashes are the same, you know that you have an identical copy.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

WHAT'S A COOKIE?
An extensive discussion on cookies would go beyond the scope of this question. I provide an overview here since a minimal understanding can be useful to have a better understanding of how and why SECRET_KEY is useful. I highly encourage you to follow up with some personal readings on HTTP Cookies.

A common practice in web applications is to use the client (web browser) as a lightweight cache. Cookies are one implementation of this practice. A cookie is typically some data added by the server to an HTTP response by way of its headers. It's kept by the browser which subsequently sends it back to the server when issuing requests, also by way of HTTP headers. The data contained in a cookie can be used to emulate what's called statefulness, the illusion that the server is maintaining an ongoing connection with the client. Only, in this case, instead of a wire to keep the connection "alive", you simply have snapshots of the state of the application after it has handled a client's request. These snapshots are carried back and forth between client and server. Upon receiving a request, the server first reads the content of the cookie to reestablish the context of its conversation with the client. It then handles the request within that context and before returning the response to the client, updates the cookie. The illusion of an ongoing session is thus maintained.

What does a cookie look like?
A typical cookie would look like this:

name: _profile
content: uid=382|status=genie
domain: .example.com
path: /
send for: Encrypted connections only
expires: July 1 2030, 1:20:40 AM UTC
Cookies are trivial to peruse from any modern browser. On Firefox for example go to Preferences > Privacy > History > remove individual cookies.

The content field is the most relevant to the application. Other fields carry mostly meta instructions to specify various scopes of influence.

Why use cookies at all?
The short answer is performance. Using cookies, minimizes the need to look things up in various data stores (memory caches, files, databases, etc), thus speeding things up on the server application's side. Keep in mind that the bigger the cookie the heavier the payload over the network, so what you save in database lookup on the server you might lose over the network. Consider carefully what to include in your cookies.

Why would cookies need to be signed?
Cookies are used to keep all sorts of information, some of which can be very sensitive. They're also by nature not safe and require that a number of auxiliary precautions be taken to be considered secure in any way for both parties, client and server. Signing cookies specifically addresses the problem that they can be tinkered with in attempts to fool server applications. There are other measures to mitigate other types of vulnerabilities, I encourage you to read up more on cookies.

How can a cookie be tampered with?
Cookies reside on the client in text form and can be edited with no effort. A cookie received by your server application could have been modified for a number of reasons, some of which may not be innocent. Imagine a web application that keeps permission information about its users on cookies and grants privileges based on that information. If the cookie is not tinker-proof, anyone could modify theirs to elevate their status from "role=visitor" to "role=admin" and the application would be none the wiser.

Why is a SECRET_KEY necessary to sign cookies?
Verifying cookies is a tad bit different than verifying source code the way it's described earlier. In the case of the source code, the original author is the trustee and owner of the reference fingerprint (the checksum), which will be kept public. What you don't trust is the source code, but you trust the public signature. So to verify your copy of the source you simply want your calculated hash to match the public hash.

In the case of a cookie however the application doesn't keep track of the signature, it keeps track of its SECRET_KEY. The SECRET_KEY is the reference fingerprint. Cookies travel with a signature that they claim to be legit. Legitimacy here means that the signature was issued by the owner of the cookie, that is the application, and in this case, it's that claim that you don't trust and you need to check the signature for validity. To do that you need to include an element in the signature that is only known to you, that's the SECRET_KEY. Someone may change a cookie, but since they don't have the secret ingredient to properly calculate a valid signature they cannot spoof it. As stated a bit earlier this type of fingerprinting, where on top of the checksum one also provides a secret key, is called a Message Authentication Code.

What about Sessions?
Sessions in their classical implementation are cookies that carry only an ID in the content field, the session_id. The purpose of sessions is exactly the same as signed cookies, i.e. to prevent cookie tampering. Classical sessions have a different approach though. Upon receiving a session cookie the server uses the ID to look up the session data in its own local storage, which could be a database, a file, or sometimes a cache in memory. The session cookie is typically set to expire when the browser is closed. Because of the local storage lookup step, this implementation of sessions typically incurs a performance hit. Signed cookies are becoming a preferred alternative and that's how Flask's sessions are implemented. In other words, Flask sessions are signed cookies, and to use signed cookies in Flask just use its Session API.

Why not also encrypt the cookies?
Sometimes the contents of cookies can be encrypted before also being signed. This is done if they're deemed too sensitive to be visible from the browser (encryption hides the contents). Simply signing cookies however, addresses a different need, one where there's a desire to maintain a degree of visibility and usability to cookies on the browser, while preventing that they'd be meddled with.

What happens if I change the SECRET_KEY?
By changing the SECRET_KEY you're invalidating all cookies signed with the previous key. When the application receives a request with a cookie that was signed with a previous SECRET_KEY, it will try to calculate the signature with the new SECRET_KEY, and both signatures won't match, this cookie and all its data will be rejected, it will be as if the browser is connecting to the server for the first time. Users will be logged out and their old cookie will be forgotten, along with anything stored inside. Note that this is different from the way an expired cookie is handled. An expired cookie may have its lease extended if its signature checks out. An invalid signature just implies a plain invalid cookie.

So unless you want to invalidate all signed cookies, try to keep the SECRET_KEY the same for extended periods.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
What's a good SECRET_KEY?
A secret key should be hard to guess. The documentation on Sessions has a good recipe for random key generation:

CREATING A SECRET_KEY
>>> import os
>>> os.urandom(24)
'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
You copy the key and paste it in your configuration file as the value of SECRET_KEY.

Short of using a key that was randomly generated, you could use a complex assortment of words, numbers, and symbols, perhaps arranged in a sentence known only to you, encoded in byte form.

Do not set the SECRET_KEY directly with a function that generates a different key each time it's called. For example, don't do this:

# this is not good
SECRET_KEY = random_key_generator()
Each time your application is restarted it will be given a new key, thus invalidating the previous.

Instead, open an interactive python shell and call the function to generate the key, then copy and paste it to the config.

Share
Follow
edited Aug 25 at 18:12
Abhishek Madhu's user avatar
Abhishek Madhu
3077 bronze badges
answered Feb 3, 2018 at 11:29
Michael Ekoka's user avatar
Michael Ekoka
19.4k1212 gold badges7979 silver badges7979 bronze badges
"Do not set the SECRET_KEY directly with a function that generates a different key each time it's called...Instead, open an interactive python shell and call the function to generate the key, then copy and paste it to the config." And why is that? So it is better to have a secret in plain text in a file? – 
Hugo Sousa
 Sep 18, 2020 at 9:21
2
@HugoSousa Explanations for keeping the key constant are given in the section What happens if I change the SECRET_KEY? Discussions on how to keep application configuration secure, although useful, are a separate topic that I believe to be beyond scope. But I encourage anyone with the same concerns to search for advices in that specific direction. – 
Michael Ekoka
 Sep 18, 2020 at 16:13
Is there a use case when one needs to use SECRET_KEY 'manually' for example as Admin user? I mean one can in principle make a config file containing SECRET_KEY=generate_random_key(), this key is generated once but is not given in plain text. – 
Fedor Petrov
 Jun 29, 2021 at 7:36
Add a comment
126

Anything that requires encryption (for safe-keeping against tampering by attackers) requires the secret key to be set. For just Flask itself, that 'anything' is the Session object, but other extensions can make use of the same secret.

secret_key is merely the value set for the SECRET_KEY configuration key, or you can set it directly.

The Sessions section in the Quickstart has good, sane advice on what kind of server-side secret you should set.

Encryption relies on secrets; if you didn't set a server-side secret for the encryption to use, everyone would be able to break your encryption; it's like the password to your computer. The secret plus the data-to-sign are used to create a signature string, a hard-to-recreate value using a cryptographic hashing algorithm; only if you have the exact same secret and the original data can you recreate this value, letting Flask detect if anything has been altered without permission. Since the secret is never included with data Flask sends to the client, a client cannot tamper with session data and hope to produce a new, valid signature.

Flask uses the itsdangerous library to do all the hard work; sessions use the itsdangerous.URLSafeTimedSerializer class with a customized JSON serializer.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

REFER TO THE APP OBJECT IN VIEW THAT WAS INITIALIZED IN A SEPARATE FILE (e.g., __init__.py)

from flask import Blueprint, current_app

bp = Blueprint('my_blueprint', __name__)

@bp.route('/')
def my_view():
    with current_app.app_context():
        app_name = current_app.name
        app_config = current_app.config
        # Your code here

NOTES ABOUT FLASK APP.APP_CONTEXT
app.app_context() is a method in Flask that returns an application context for the current application. The application context keeps track of the application-level data during a request, CLI command, or other activity 1.

The app.app_context() method is typically used to access the Flask application object within views and CLI commands. However, importing the app instance within the modules in your project is prone to circular import issues. When using the app factory pattern or writing reusable blueprints or extensions there won’t be an app instance to import at all. Flask solves this issue with the application context. Rather than referring to an app directly, you use the current_app proxy, which points to the application handling the current activity 1.

If you try to access current_app, or anything that uses it, outside an application context, you’ll get a RuntimeError with the message “Working outside of application context”. To solve this, you can set up an application context with app.app_context(). You can use app_context() in a with block, and everything that runs in the block will have access to current_app 1.

GET A USER ID TO STORE IN FLASK SESSION

To get a user ID to store in a Flask session, you can use Flask-Login to manage user authentication and sessions. Flask-Login provides a current_user object that represents the current user, and you can use the get_id() method of this object to get the user ID.

Here’s an example code snippet that demonstrates how to get the user ID and store it in a Flask session:

from flask import Flask, session
from flask_login import LoginManager, UserMixin, login_user, current_user

app = Flask(__name__)
app.secret_key = 'my_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login')
def login():
    user = User('john.doe')
    login_user(user)
    session['user_id'] = current_user.get_id()
    return 'Logged in successfully!'

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return 'Logged out successfully!'

@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    if user_id:
        return f'User ID: {user_id}'
    else:
        return 'User not logged in!'
        
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
It is generally not recommended to store bearer tokens in session objects. Bearer tokens are typically used for short-term authentication and authorization purposes and should not be stored for long periods of time 123.

Instead, you should consider using a more secure and scalable method for storing and managing bearer tokens. For example, you can store the bearer token in a secure cookie or use a token management service such as OAuth 2.0 or OpenID Connect to manage your tokens 123.

If you need to store user-specific data, you can use a session object to store the data instead of the bearer token. Flask provides a built-in session management system that you can use to store user-specific data in a secure and scalable way 4

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
USER ID

In the context of a Flask session, a user ID is a unique identifier that is used to identify a user across multiple requests. Flask sessions work by generating a unique session ID for each user who accesses your web application. This session ID is typically stored as a cookie in the user’s browser, allowing the server to identify the user on subsequent requests. The server can then use this session ID to store and retrieve data associated with that particular user 12.

To create a user ID in Flask, you can use the uuid module to generate a unique ID for each user. Here’s an example code snippet that demonstrates how to generate a unique ID and store it in the Flask session:

from flask import Flask, session
import uuid

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    user_id = str(uuid.uuid4())
    session['user_id'] = user_id
    return f'User ID: {user_id}'

In this example, we create a Flask app and use the uuid.uuid4() method to generate a unique ID for each user. We then store the user ID in the Flask session using the session object.

Please note that this is just an example and you should modify the code to suit your specific needs. Also, make sure to keep your secret key secret and secure to prevent unauthorized access to your session data 12
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATING, SENDING AND RETRIEVING COOKIES

To create a cookie using a Flask session object, return it as a cookie, and then retrieve it from the cookie on a subsequent request, you can follow these steps:

First, import the make_response function from the flask module.
from flask import make_response

Next, use the make_response function to create a response object.
response = make_response('Hello, World!')

To set a cookie in the response header, use the set_cookie method of the response object. The set_cookie method takes the name of the cookie, the value of the cookie, and any optional parameters such as the cookie’s expiration time.
response.set_cookie('my_cookie', 'my_value', max_age=3600)

To retrieve the cookie from the subsequent request, use the request.cookies dictionary. The request.cookies dictionary contains all the cookies sent by the client in the request.
my_cookie = request.cookies.get('my_cookie')

Here’s an example code snippet that demonstrates how to create a cookie using a Flask session object, return it as a cookie, and then retrieve it from the cookie on a subsequent request:

from flask import Flask, make_response, request, session

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    session['my_data'] = 'Hello, World!'
    response = make_response('Hello, World!')
    response.set_cookie('my_cookie', 'my_value', max_age=3600)
    return response

@app.route('/get_cookie')
def get_cookie():
    my_data = session.get('my_data')
    my_cookie = request.cookies.get('my_cookie')
    return f'My data: {my_data}, My cookie: {my_cookie}'

In this example, we create a Flask app and use the session object to store some data. We then create a response object using the make_response function and set a cookie in the response header using the set_cookie method. Finally, we retrieve the cookie from the subsequent request using the request.cookies dictionary.

Please note that this is just an example and you should modify the code to suit your specific needs. Also, make sure to keep your secret key secret and secure to prevent unauthorized access to your session data 12.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

SEND A COOKIE BACK IN A RESPONSE HEADER

To send a cookie back in a response header, you can use the set_cookie method of the flask.Response object. The set_cookie method takes the name of the cookie, the value of the cookie, and any optional parameters such as the cookie’s expiration time.

Here’s an example code snippet that demonstrates how to send a cookie back in a response header:
from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    response = Response('Hello, World!')
    response.set_cookie('my_cookie', 'my_value')
    return response

SEND A RESPONSE HEADER ALONG WITH A JSON OBJECT BACK TO A USER

To send a response header along with a JSON object in Flask, you can use the make_response function to create a response object and set the headers using the headers attribute of the response object. Here’s an example code snippet that demonstrates how to send a response header along with a JSON object:

from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def index():
    data = {'message': 'Hello, World!'}
    response = make_response(jsonify(data))
    response.headers['X-My-Header'] = 'my_value'
    return response

In this example, we create a Flask app and use the jsonify function to create a JSON object. We then use the make_response function to create a response object and set the X-My-Header header using the headers attribute of the response object.

Please note that you should modify the code to suit your specific needs. Also, make sure to keep your secret key secret and secure to prevent unauthorized access to your session data 12.

When a server wants to send a cookie to a client, it can do so by setting the Set-Cookie header in the response. The Set-Cookie header contains the name and value of the cookie, as well as optional attributes such as the cookie’s expiration date, domain, and path. Here is an example of how to set a cookie in a response header:
HTTP/1.1 200 OK
Content-Type: text/html
Set-Cookie: name=value; expires=Wed, 21 Dec 2023 13:25:08 GMT; path=/


In this example, the Set-Cookie header sets a cookie named name with a value of value. The expires attribute specifies when the cookie should expire, and the path attribute specifies the URL path for which the cookie is valid.

When the client receives the response, it stores the cookie and sends it back to the server with subsequent requests using the Cookie header. Here is an example of how to send a cookie in a request header:
GET / HTTP/1.1
Host: example.com
Cookie: name=value

USING SIGNED COOKIES

from flask import Flask, request, make_response
import hashlib
import hmac

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def sign_cookie(data):
    secret_key = app.secret_key.encode('utf-8')
    signature = hmac.new(secret_key, data.encode('utf-8'), hashlib.sha256).hexdigest()
    return f"{data}|{signature}"

def unsign_cookie(cookie):
    data, signature = cookie.split('|')
    expected_signature = hmac.new(app.secret_key.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()
    if signature != expected_signature:
        raise ValueError('Invalid signature')
    return data

@app.route('/')
def index():
    if 'username' in request.cookies:
        username = unsign_cookie(request.cookies['username'])
        return f'Logged in as {username}.'
    return 'You are not logged in.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session_cookie = sign_cookie(username)
        response = make_response(redirect('/'))
        response.set_cookie('username', session_cookie)
        return response
    return '''
        <form method="post">
            <p><input type="text" name="username"></p>
            <p><input type="submit" value="Login"></p>
        </form>
    '''

@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('username')
    return response

In the example above, we have defined three routes: /, /login, and /logout. The / route checks if the username key is present in the request.cookies dictionary. If it is, it displays a message saying that the user is logged in. If not, it displays a message saying that the user is not logged in.

The sign_cookie function takes a string and returns a signed cookie string. The unsign_cookie function takes a signed cookie string and returns the original string if the signature is valid, or raises a ValueError if the signature is invalid.

The /login route accepts both GET and POST requests. If it receives a POST request, it signs the username value using the sign_cookie function and sets a cookie with the signed value. It then redirects the user to the / route. If it receives a GET request, it displays a login form.

The /logout route deletes the username cookie and redirects the user to the / route.


EXAMPLE OF USING JAVASCRIPT TO PASS CREDENTIALS TO API
const data = { key1: 'value1', key2: 'value2' };
const options = {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data)
};

fetch('https://example.com/api', options)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));


VARIOUS URLs
    url = 'http://127.0.0.1:8300/api/Users/v1/login'
    url = 'https://ltc-dev-server.vercel.app/api/Users/v1/login'
    url = 'https://py-http-server.vercel.app/login'
    url = 'https://testapi.latax.la.gov/api/Auth/v1/authenticate'#   url = 'https://testapi.latax.la.gov/api/Auth/v1/authenticate?param=value&param2=value'
    url = 'https://api.latax.la.gov/api/Auth/v1/authenticate?param=value&param2=value'
    url = 'https://testserver-chrism.pythonanywhere.com/api/Users/v1/login'

GENERATE AN SSH KEY IN WINDOWS:

    Generate SSH Key Pair on Windows:
Open Windows PowerShell (you can search for it in the Start menu).
Run the following command to generate an RSA key pair:
ssh-keygen -t rsa -b 4096

This command will create a public key (id_rsa.pub) and a private key (id_rsa) in your user’s home directory (usually C:\Users\your_username).
Copy the Public Key to the Debian Server:
Log in to your Debian server using your existing credentials (password-based authentication).
Once logged in, create the .ssh directory in your home folder (if it doesn’t exist):
mkdir ~/.ssh

Copy the content of your local public key (id_rsa.pub) to the ~/.ssh/authorized_keys file on the server:
echo "YOUR_PUBLIC_KEY_CONTENT" >> ~/.ssh/authorized_keys

Replace YOUR_PUBLIC_KEY_CONTENT with the actual content of your local public key.
Set Correct Permissions:
Ensure that the permissions for the .ssh directory and the authorized_keys file are secure:
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

Test SSH Connection:
Now you can try connecting to your Debian server using SSH keys:
ssh username@your_server_ip

Replace username with your actual username on the server and your_server_ip with the server’s IP address or hostname.
You should be able to log in without entering a password.
Optional: Disable Password Authentication (Recommended for Security):
Once you’ve confirmed that SSH key-based authentication works, consider disabling password authentication to enhance security.
Edit the SSH server configuration file (/etc/ssh/sshd_config) on the Debian server:
sudo nano /etc/ssh/sshd_config

Find the line that says PasswordAuthentication yes and change it to PasswordAuthentication no.
Save the file and restart the SSH service:
sudo systemctl restart ssh


INSTALL PYTHON

Download the Tar File: Visit the official Python website at python.org/downloads and navigate to the Downloads section. Choose the desired Python version (in this case, Python 3.10.6) and select the corresponding Gzipped source tarball (.tgz file).
Extract the Tgz File: Once the tar file is downloaded, open a terminal or command prompt and navigate to the directory where the file is saved. Use the tar command to extract the contents of the tar file. For example:
tar xzf Python-3.10.6.tgz
cd Python-3.10.6

Configure the Installation: Navigate into the extracted directory:
cd Python-3.10.6
Next, run the configure script to prepare the installation. This step ensures that the necessary dependencies are detected and sets up the installation according to your system’s configuration:
./configure \
    --prefix=/opt/python/3.10.6 \
    --enable-shared \
    --enable-optimizations \
    --enable-ipv6 \
    LDFLAGS=-Wl,-rpath=/opt/python/3.10.6/lib,--disable-new-dtags

Build and Install Python: After the configuration step is complete, proceed to build and install Python on your system. Use the following commands:
make
sudo make install
The make command compiles the source code, and make install installs Python onto your system. The sudo command ensures that the installation has the necessary permissions.
Verify the Installation: Confirm that Python is installed correctly by opening a new terminal or command prompt window and executing the following command:
/opt/python/3.10.6/bin/python3.10 --version
You should see the installed Python version printed on the screen.
Make Your New Version Default (optional): To make the newly installed Python version your default, create a symbolic link:
cd /opt/python/3.10.6/bin
sudo ln -s python3.10 python
echo "PATH=/opt/python/3.10.6/bin:$PATH" >> ~/.profile
. ~/.profile
Now you can use python to refer to Python 3.10.6.
Remember to adjust paths and filenames as needed. Enjoy coding with Python 3.10.6! 🐍🚀

This method is particularly useful in offline environments or when you require a specific Python version that may not be available in your package manager1.


DIRECTORY STRUCURE THAT INCLUDES FRONTEND FILES

my_flask_react_project/
├── my_flask_app/
│   ├── app.py
│   ├── templates/
│   │   ├── base.html
│   │   └── ...
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── ...
│   └── ...
├── client/
│   ├── package.json  # Place your package.json here
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   └── ...
│   ├── public/
│   │   ├── index.html
│   │   └── ...
│   └── ...
└── venv/

LOGGING (https://www.youtube.com/watch?v=urrfJgHwIJA&t=6s)

    import logging

    # Various levels
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critcal("critcal')

    # By default you only get the output of anything avouv warning. debug and info won't
    # SAMPLE OUTPT:
        ERROR:root:error (root refers to the root logger, not user)

    Sending logging output to a file:

        logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w") # ONLY DO THIS ONE TIME, USUALLY AT PROGRAM START

        A MORE ADVANCED WAY:
            logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w".
                    foramt="%(asctime)s - %(levelname)s - %(message)s")

    x = 2 # Logging the value of a variable
    logging.info(f"the value of x is {x}")

    STACK TRACE

        try:
            1 / 0
        except ZeroDivisiion as e:
            logging.erro("ZeroDivisonError", exc_info=True)
                        OR
            logging.exception("whatever")

    Custom Logs:
        logger = logging.getLogger("name") # 'naem is the name of the logger that you want. If this logger name exists it will just give it to you, otherwise it will create it.

        The convention is to use one logger per module and use: logger = logging.getLogger('__name__') # dunder name will give name of cureent module.
        
        #setup a handler to allow you to write to sepearate log file than what was created using basicConfig()
        handler = logging.FileHandler('test.log') # all of available Handlers (HTTP, email, etc)
        #setup a formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        logger.info("test the custom logger")

    TDD Workflow
    (https://www.youtube.com/watch?v=ibVSPVz2LAA)
    
        The Three Laws of TDD
            TDD or Test Driven Development is a set of programming and software design principles, based on a cycle of:    
                fail test -> fix code -> pass test -> fail new test ...

                1. You may not write any production code unless you've first written a failing unit test (Robert C. Martin Uncle Bob)
                2  You may not write more of a unit test than is sufficient to fail.  (Robert C. Martin Uncle Bob)
                3. You may not write more production code than is sufficient to make the failing unit test pass  (Robert C. Martin Uncle Bob)
                    - Ask yourself, 'what is the least I can do to fix my code at the bare minimum'
        EXAMPLE:
            Ceasar's Cipher

            import unittest
            import string

            def encrypt(message):
                abc = string.ascii_letters + string.punctuation  + string.digits + " "
                encrypted_message = "".join([abc[abc.find(char) + 1 ] if len(abc) > (abc.find(char) + 1) else abc[0] for idx, char in enumerate(message)])
                return encrypted_message

            class TestEncryption(unittest.TestCase):
                # tests go here. with each of our tests we are aiming to evaluate a boolean experssion (aka: assertions)
                def setUp(self):
                    self.my_message = "banana"

                def test_inputExists(self): # test_ is required
                    self.asseertIsNotNone(self.my_message)
                    # At this point, without my_message being defined, we have met the first two rules above
                    # To meet the 3rd rule, assign a value to my_message. To do so, do it in a special method
                    # called setUp() see above.

                def test_inputType(self):
                    self.assertIsInstance(self.my_message, str)
                    # Will fail test while value isset to 0. Change it to a string

                def test_functionReturnsSomething(self): # test_ is required
                    self.asseertIsNotNone(encrypt(self.my_message))
                    # encrypt is the function we are testing to see if it returns a value. It will fail now because it doesn't exit

                def test_lenIO(self):
                    self.assertEqual(len(self.my_message), len(encrypt(self.my_message)))
                    # will fail, which satisifies 1, and 2 and will pass once the return value of 0
                    # is replaced with the 'message' in the encrypt function above.

                def test_differentIO(self):
                    self.assertNotIn(self.my_message, encrypt(self.my_message))

                def test_outputType(self):
                    self.assertIsInstance(encrypt(self.my_message), str)

                def test_shiftedCipher(self):
                    abc = string.ascii_letters + string.punctuation  + string.digits + " "
                    encrypted_message = "".join([abc[abc.find(char) + 1 ] for idx, char in enumerate(self.my_message)])
                    print(encrypted_message)
                    self.assertEqual(encrypted_message, encrypt(self.my_message))



            if __name__ == '__main__':
                unittest.main()

            # IF YOU ARE USING JUPYTER REPLACE the above line with:
                unittest.main(argv=[''], verbosity=2, exit=False)


MOCK OBJECTS

    import requests # may need to pip install this
    import unittest
    from import unittest.mock import patch, Mock, ANY
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText


    def send_email(smtp_server, smtp_port, from_addr, to_addre,subject, body):
        # As, this is not a mock funtion. It is a real function that would work
        # if you passed it the proper values

        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_addr, "MyPassword")
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        server.quit()

    class TestEmail(unittest.TestCase):
        @patch('smtplib.SMTP')
        def test_send_mail(self, mock_smtp):
            # @patch allows a mock server to be created
            # when the smtplib.SMTP() method is called above
            instance = mock_smtp.return_value

            send_email("smtp.example.com", 587, "mymail@example.com", "hismail@example.com", "Subject", "Mail Content")

            mock_smtp.assert_called_with("smtp.example.com",587)

            instance.starttls.assert_called_with()
            instance.login.assert_called_with("mymail@example.com", "MyPassword")
            instance.sendmail.assert_called_with("mymail@example.com", "hismail@example.com", ANY)
            instance.quit.assert_called_with()
            


    def get_user_data(user_id):
        response = requests.get(f"https://api.example.com/users/{user_id}")

        return response.json()

    class TestUserData(unittest.TestCase):

        @patch('request.get')
        def test_get_user_data(self, mock_get):
            mock_response = Mock()
            # What the mock will return
            response_dict = {'name': 'John', 'email': 'john@example.com'}
            mock_response.json.return_value = response_dict

            mock_get.return_value = mock_response

            user_data = get_user_data(1)
            mock_get.assert_called_with("https://api.example.com/users/1")
            self.assertEqual(user_data, response_dict)

if __name__ == '__main__':
    unittest.main()

CONNECTING FLASK TO REACT:

https://dev.to/ondiek/connecting-a-react-frontend-to-a-flask-backend-h1o
https://www.geeksforgeeks.org/how-to-connect-reactjs-with-flask-api/


Werkzeug implements WSGI, the standard Python interface between applications and servers.
Jinja is a template language that renders the pages your application serves
MarkupSafe comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks
ItsDangerous securely signs data to ensure its integrity. This is used to protect Flask's session cookie.
Click is a framework for writing command-line applications. It provides the flask command allows adding custom management commands.

CORS & VIDEOS

https://stackoverflow.com/questions/69963975/how-to-set-cookie-from-flask-to-reactjs

https://www.youtube.com/watch?v=34wC1C61lg0

https://www.youtube.com/watch?v=PNtFSVU-YTI&t=233s