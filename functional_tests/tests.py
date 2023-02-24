from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from blog.models import Article
from datetime import datetime
import pytz
import os


class BasicInstallTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        # staging_server = os.environ.get('STAGING_SERVER')
        # if staging_server:
        #     self.live_server_url = 'http://' + staging_server

        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summary 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-1',
        )

    def tearDown(self):
        self.browser.quit()


    def test_home_page_blog(self):
        self.browser.get(self.live_server_url)
        article_list = self.browser.find_element(By.CLASS_NAME, "article-list")
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(By.CLASS_NAME, "article-title")
        article_summary = self.browser.find_element(By.CLASS_NAME, "article-summary")
        self.assertTrue(article_summary)
        self.assertTrue(article_title)

    def test_home_page_article_title_link_leads_to_article_page(self):
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(By.CLASS_NAME, "article-title")
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        article_link_text = article_link.text

        self.browser.get(article_link.get_attribute('href'))
        article_page_title = self.browser.find_element(By.CLASS_NAME, "article-title")
        article_page_title_text = article_page_title.text
        self.assertEqual(article_link_text, article_page_title_text)

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertTrue(header.location['x'] > 10)

        footer = self.browser.find_element(By.CLASS_NAME, 'footer')
        self.assertTrue(footer.location['y'] > 500)

    def test_python_landing_redirect(self):
        self.browser.get(self.live_server_url + '/python')
        self.assertIn('Python — Википедия', self.browser.title)

    def test_setup_landing_redirect(self):
        self.browser.get(self.live_server_url + '/setup')
        self.assertIn('The web framework for perfectionists with deadlines | Django', self.browser.title)
