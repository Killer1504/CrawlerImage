from icrawler.builtin import GoogleImageCrawler
import os

def crawl_image(key_word, max_number_image, path_save):
    if os.path.exists(path_save) == False:
        raise Exception("dir save does't exists")
    google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=1,
    downloader_threads=4,
    storage={'root_dir': path_save})
    filters = dict(
        size='large',
        color='color',
        license='commercial,modify',
        date=((2010, 1, 1), None))
    google_crawler.crawl(keyword=key_word, filters=filters, offset=0, max_num=max_number_image,
                        min_size=(100,100), max_size=None, file_idx_offset=0, overwrite=True)