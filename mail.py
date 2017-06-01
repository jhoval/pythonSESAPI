##import boto library
import boto.ses

##add aws keys
AWS_ACCESS_KEY = 'YOUR-ACCESS-KEY-HERE'
AWS_SECRET_KEY = 'YOUR-SECRET-KEY-HERE'


class Email(object):
    def __init__(self, to, subject):
        self.to = to
        self.subject = subject
        self._html = None
        self._text = None
        self._format = 'html'

    def html(self, html):
        self._html = html

    def text(self, text):
        self._text = text

    def send(self, from_addr=None):
        body = self._html

        if isinstance(self.to, basestring):
            self.to = [self.to]
        if not from_addr:
            from_addr = 'test@example.com'
        if not self._html and not self._text:
            raise Exception('You must provide a text or html body.')
        if not self._html:
            self._format = 'text'
            body = self._text

##uses boto to connect AWS API REGION using credentials
        connection = boto.ses.connect_to_region(
            'us-east-1',
            aws_access_key_id='YOUR-ACCESS-KEY-HERE',
            aws_secret_access_key='YOUR-SECRET-KEY-HERE'
        )

        return connection.send_email(
            from_addr,
            self.subject,
            None,
            self.to,
            format=self._format,
            text_body=self._text,
            html_body=self._html
        )

##sends the mail to receiver
email = Email(to='receiver@example.com', subject='Here comes the subject!')
email.text('This is the text of the body. Surprise!')
email.html('<html><body>This is the text of the body. <strong>Surprise!</strong></body></html>')  # Optional
email.send()
