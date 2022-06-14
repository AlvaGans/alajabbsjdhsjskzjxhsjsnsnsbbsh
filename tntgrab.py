from concurrent.futures import ThreadPoolExecutor

from requests import get
from bs4 import BeautifulSoup as bs
from rich.console import Console
from random import choice

c = Console()

class Rev:

    def __init__(self) -> None:
        self.url = "https://domains.tntcode.com/?domain_name_box={}&domain_name_box_2=&whois_status_box=&whois_email_box=&min_rank_box=&max_rank_box=&maximum_records_box=10000&maximum_characters_box=&availability_box=any&sort=&order="
        self.domains = []
        self.domen = []
        self.keyword = ["box", "office"]
        self.result = "result.txt"

    def grab(self, keyword: str) -> int:
        try:
            res = 0
            parse = bs(get(self.url.format(keyword)).text, "html.parser")
            if parse.textarea:
                for x in parse.select("textarea")[2].text.strip().splitlines():
                    self.domains.append(x)
                    self.domen.append(x)
                    open(self.result, "a+").write(x+"\n")
                res = self.domen.__len__()
            self.domen = []
            return res
        except Exception as e:
            print(e)
            return 0

    def animation(self, task: list, title: str, type: str="rev") -> None:
        with c.status("[cyan]%s" % title) as tod:
            with ThreadPoolExecutor(max_workers=self.thread) as thread:
                for tosk in task:
                    if type == "grab":
                        anu = thread.submit(self.grab, tosk).result()
                        spin = choice(["aesthetic","bouncingBall","bouncingBar","arc"])
                        if anu == 0:
                            tod.update("[cyan]%s[white] Grabbed - [red]%s [white]domain(s)" % (tosk, anu), spinner=spin)
                        else:
                            tod.update("[cyan]%s[white] Grabbed - [green]%s [white]domains(s)" % (tosk, anu), spinner=spin)
                    elif type == "write":
                        open(self.result, "a+").write(tosk+"\n")

    @property
    def main(self):
        self.keyword = open(input("Keyword List : ")).read().splitlines()
        self.result = input("Saved : ")
        self.thread = int(input("Thread : "))
        self.animation(list(dict.fromkeys(self.keyword)), "Grab Domains", "grab")
        #self.animation(self.domains, "Writing domains on file [cyan]%s" % self.result, "write")
        c.print("[green]Successfully [white]File saved in [green]%s" % self.result)

if __name__ == "__main__":
    Rev().main
