import scraper as sp

def main():
    scraper = sp.scraper()
    scraper.config_user("lukezim5", "playlist-read-private", "3035253db48b41bc9d5054646ff3cac5", "163471d7285c4fe58fb90573b5042bc6")
    scraper.get_featured_playlists()
    return

main()