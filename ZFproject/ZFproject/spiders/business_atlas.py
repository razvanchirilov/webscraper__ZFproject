import scrapy
import json
import urllib.request
import ssl

class BusinessAtlasSpider(scrapy.Spider):
    name = "business_atlas"
    allowed_domains = ["edition.pagesuite.com"]
    start_urls = ["https://edition.pagesuite.com/html5/reader/get_page_groups_from_eid.aspx?pubid=693e0aa3-c075-4826-b030-e30100eee5c5&eid=e5d8807a-ac5e-4033-bf64-22eb37832e8d&lm=63816824779650&version=production"]

    # Disable SSL verification
    ssl._create_default_https_context = ssl._create_unverified_context

    def parse(self, response):
        data = json.loads(response.body)
        images_urls = []
        for page_group in data['pageGroups']:
            for page in page_group['pages']:
                images_urls.append(page['pdf'])

        # Download the images
        for i, url in enumerate(images_urls):
            filename = f"data_images/image{i+1}.pdf"
            urllib.request.urlretrieve(url, filename)
            self.log(f"Downloaded image {i+1} from URL {url}")

