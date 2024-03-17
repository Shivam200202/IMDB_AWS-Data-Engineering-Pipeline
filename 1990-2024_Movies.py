import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


name  = []
year  = []
pg    = []
rnt   = []

genre = []
com   = []
drama = []
act   = []
rom   = []
bio   = []
crime = []
myst  = []
hor   = []
anima = []
scifi = []
adven = []
thiri = []

imdbr = []

Meta_Score_Type = []
Score = []

summr = []
dirn  = []
stars = []
votes = []
gross = []

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
for a in range(1,13):
    url = requests.get(f'https://www.imdb.com/list/ls560109468/?sort=list_order,asc&st_dt=&mode=detail&page={a}', headers = headers).text

    soup = BeautifulSoup(url, 'html.parser')
    bsoup = soup.find_all('div', class_ = 'lister-item mode-detail')


    for i in bsoup:

    #Name
        n = i.h3.a.text.strip()
        name.append(n)

    #year
        y = i.find('span', class_ = 'lister-item-year text-muted unbold').text
        y = re.sub(r'[\(\)A-Z]',"", y).strip()
        y1 = lambda x: (0 if y =="" else y)
        year.append(y1(y))

    #PG
        p_span = i.find('span', class_='certificate')
        if p_span:
            p = p_span.text.strip()

        else:
            p = 0
        pg.append(p)

    #Run Time
        rt = i.find('span', class_ = 'runtime')
        if rt:
            rt = rt.text.strip()
        else:
            rt = 0

        rnt.append(rt)

    #Genre
        g = i.find('span', class_ = 'genre').text.strip()
        genre.append(g)

    #Detailed Genre
    #Lambda function to check if ''Comedy'' is present in the list of genres
        co = lambda x: (1 if 'Comedy' in x.split(', ') else 0)


        com.append(co(g))

        dr = lambda x: (1 if 'Drama' in g.split(', ') else 0)
        drama.append(dr(g))

        ac = lambda x: (1 if 'Action' in g.split(", ") else 0)
        act.append(ac(g))

        ro = lambda x: (1 if 'Romance' in g.split(", ") else 0)
        rom.append(ro(g))

        bi = lambda x: (1 if "Romance" in g.split(", ") else 0 )
        bio.append(bi(g))

        cri = lambda x: (1 if "Crime" in g.split(", ") else 0)
        crime.append(cri(g))

        mys = lambda x: (1 if "Mystery" in g.split(", ") else 0)
        myst.append(mys(g))

        ho = lambda x: (1 if "Horror" in g.split(", ") else 0)
        hor.append(ho(g))

        ani = lambda x: (1 if "Animation" in g.split(", ") else 0)
        anima.append(ani(g))

        sci = lambda x: (1 if "Sci-Fi" in g.split(", ") else 0)
        scifi.append(sci(g))

        adv = lambda  x: (1 if "Adventure" in g.split(", ") else 0)
        adven.append(adv(g))

        thi = lambda x: (1 if "Thriller" in g.split(", ") else 0)
        thiri.append(thi(g))


    ##IMDB Rating
        imd = i.find("span", class_ = "ipl-rating-star__rating")
        if imd:
            imd = imd.text.strip()
        else:
            imd = 0
        imdbr.append(imd)


    #Meta Score
        metascore_span = i.find('span', 'metascore')
        if metascore_span:
            if "favorable" in metascore_span["class"]:
                mst = "favorable"
                sc = int(i.find("span", class_ = "metascore").text.strip())
            elif 'mixed' in metascore_span["class"]:
                mst = "mixed"
                sc = int(i.find("span", class_ = "metascore").text.strip())

            elif 'unfavorable' in metascore_span["class"]:
                mst = 'unfavorable'
                sc = int(i.find("span", class_ = "metascore").text.strip())
            else:
                mst = 0
                sc  = 0
        else:
            mst = "No MetaScore"
            s   = 0


        Meta_Score_Type.append(mst)
        Score.append(sc)

    #Summary
        summ = i.find('p', class_ = "").text.strip()
        summr.append(summ)

    #Diretor Name
        ca = i.find_all('p')[2].text.strip().replace('Director:\n', "").replace('Directors:\n', "").replace("    Stars:\n", "").replace("\n", "")
        cast = ca.split("| ")

        dir = cast[0]
        dirn.append(dir)

    ##Star Name
        star = cast[1]
        stars.append(star)

    #Votes
        p_tags = i.find_all('p')
        if len(p_tags) > 3:
            span_tags = p_tags[3].find_all('span')
            if len(span_tags) > 1:
                vote = span_tags[1].text.strip()
            else:
                vote = 0
        else:
            vote =0

        votes.append(vote)

    #Gross Money

        p_tag1 = i.find_all('p')
        if len(p_tag1) >3:
            span_tag1 = p_tag1[3].find_all("span")
            if len(span_tag1) >=4:
                gros = float(span_tag1[4].text.strip().replace('$',"").replace("M", ""))
            else:
                gros = 0
        else:
            gros = 0
        gross.append(gros)

########                     DATAFRAME                      ###########
df = pd.DataFrame({"Name": name,"Year": year, "PG": pg, "Run Time": rnt, "Genre": genre, "Action": act, "Adventure": adven, "Animation": anima,
                   "Biography": bio, "Comedy": com, "Crime": crime, "Drama": drama, "Horror": hor, "Mystery": myst,
                   "Romance": rom,  "Sci-Fi": scifi, "Thiriller": thiri, "IMDB Rating": imdbr, "Meta Score Type": Meta_Score_Type,
                   "Meta Score": Score, "Summary": summr, "Director Name": dirn, "Stars": stars, "Count of Votes": votes,
                   "Gross Earning": gross})

S3 = "AWS S3 Folder URI"

df.to_csv(rf'{}\IMDB_Movies_1990-2022.csv', index = False)
