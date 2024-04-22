import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed and in your PATH

# List of links
printed_packaging_links = [
    "https://www.designtechproducts.com/articles/3d-printingpackaging#:~:text=3D%20printing%2C%20with%20its%20inherent,environment%20friendly%20material%20in%20packaging.&text=3D%20packaging%20has%20opened%20up,important%20constraints%20is%20the%20cost.",
    "https://www.stratasys.co.in/industries-and-applications/3d-printingapplications/packaging/",
    "https://www.alexanderdanielsglobal.com/blog/3d-printing-in-the-packagingindustry/",
    "https://www.3dnatives.com/en/3d-printing-sustainable-packaging-corporategoals-consumer-demands-211220214/",
    "https://zortrax.com/applications/packaging-design/",
    "https://www.prescouter.com/2017/02/3d-printing-disrupting-packaging/",
    "https://www.weareamnet.com/blog/impact-3d-printing-packaging-supply-chain/",
    "https://replique.io/2023/08/24/6-reasons-why-the-packaging-industry-should-shiftto-3d-printing/",
    "https://amfg.ai/2020/08/17/how-3d-printing-transforms-the-food-and-beverageindustry/",
    "https://www.packagingconnections.com/blog-entry/3d-printing-packaging.htm-0",
    "https://www.divbyz.com/blog/3d-printed-packaging-solutions",
    "https://www.packcon.org/index.php/en/articles/118-2022/328-3d-printing-in-thepackaging-industry",
    "https://nexa3d.com/industries/packaging/",
    "https://lekac.com/production/3-ways-3d-printing-is-disrupting-the-packagingindustry",
    "https://www.javelin-tech.com/3d/process/packaging-design/",
    "https://www.cossma.com/production/article/3d-printed-packaging-36939.html",
    "https://textilevaluechain.in/news-insights/transforming-consumer-experience-3dprinted-packaging-industry-is-the-new-big-thing-in-the-market-and-will-it-cross-us3-billion-by-2033",
    "https://www.objective3d.com.au/resource/blog/developing-sustainablepackaging-solutions-with-3d-printing-technology/",
    "https://medium.com/@sindiajohn0246/3d-printed-packaging-market-key-driversand-challenges-2023-2033-ba372b4d151e",
    "https://ieeexplore.ieee.org/document/7887895",
    "https://quickparts.com/3d-printing-for-the-packaging-industry/",
    "https://www.packagingstrategies.com/articles/104099-podcast-the-role-of-3dprinting-in-sustainable-packaging",
    "https://www.health-care-it.com/company/910976/news/3408203/shaping-thefuture-3d-printed-packaging-market-set-to-double-to-us-2-560-million-by-2033-with-a-7-8-cagr",
    "https://ijaers.com/detail/applications-and-prospects-of-3d-printing-in-thepackaging-industry/",
    "https://www.packagingdevelopments.com/blog/3d-printing-within-the-packagingprocess-a-hindrance-or-a-help/",
    "https://www.packagingdigest.com/digital-printing/3d-printing-s-future-inpackaging-is-promising",
    "https://theuniquegroup.com/impact-3d-printing-packing-industry/",
    "https://www.liquidpackagingsolution.com/news/3d-printing-the-future-ofpackaging",
    "https://www.jabil.com/blog/3d-printing-trends-show-positive-outlook.html",
    "https://replique.io/2023/08/24/6-reasons-why-the-packaging-industry-should-shiftto-3d-printing/",
    "https://www.startus-insights.com/innovators-guide/top-10-packaging-industrytrends-innovations-in-2021/",
    "https://www.printweek.in/features/various-packaging-trends-for-industryadvancements-57740",
    "https://pakfactory.com/blog/future-of-packaging-technology-design-in-the-next10-years-and-beyond/",
    "https://www.mdpi.com/2673-687X/3/1/6",
    "https://www.printweek.in/news/deconstructing-growth-in-3dprinted-packagingmarket-42523",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9818434/",
    "https://www.beautypackaging.com/issues/2020-03-01/view_features/digital-3dprinting-inspire-new-designs/",
    "https://www.researchgate.net/publication/368978658_Analysis_of_the_Applicatio n_and_Exploration_of_3D_Printing_Technology_Used_in_the_Future_Takeaway_Packaging",
    "https://www.thecustomboxes.com/blog/3d-printing-technology-and-packagingindustry/",
    "https://siliconsemiconductor.net/article/118244/Breakthroughs_and_opportunities_in_3D_packaging",
    "https://www.food.gov.uk/research/introduction-3d-printing-technologies-in-the-food-system-for-food-production-and-packaging"
]


# Function to scrape data from a webpage
def scrape_webpage(url):
    driver.get(url)
    # Scraping the first five paragraphs of text
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')
    text = '\n'.join(paragraph.text for paragraph in paragraphs[:5])
    # Scraping unique images using a set
    images = {image.get_attribute('src') for image in driver.find_elements(By.TAG_NAME, 'img')}
    images.discard(None)  # Remove any None values
    # Scraping unique links using a set
    while True:
        try:
            links = {link.get_attribute('href') for link in driver.find_elements(By.TAG_NAME, 'a')}
            links.discard(None)  # Remove any None values
            break
        except StaleElementReferenceException:
            time.sleep(1)
            continue
    return {'Site Link': url, 'All Text': text, 'Image List': ', '.join(images), 'Link List': ', '.join(links)}

# Scraping data from each link
scraped_data = []
for link in printed_packaging_links:
    scraped_data.append(scrape_webpage(link))

# Writing data to CSV
with open('scraped_printed_packaging_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Site Link', 'All Text', 'Image List', 'Link List']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(scraped_data)

# Close the WebDriver
driver.quit()

print("Data saved to 'scraped_printed_packaging_data.csv'")
