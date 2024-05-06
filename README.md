# nature-webscrape-data


data that will be used is in ./data folder

INFO:
{
        "Title": "string", // Beware spcial letter
        "Link": "string", // Link to this paper in nature.com
        "Summary": "string", // Description
        "Authors": [
            "string"
        ],              // List of Author (!! Not all of author)
        "Article Type": "string",
        "Open Access": "string",
        "Publication Date": "07 Jun 2019", //string
        "Journal Title": "string",
        "Volume and Pages": "Volume: 10, P: 1-8", // string
        "Detail": {         // Detail of paper (scrape from "Link")
            "Article Name": "string",
            "Article Link": "https://doi.org/10.1016%2Fj.ejphar.2008.10.051", //กุไม่รู้มันคือไร 555555 กุน่าจะทำไรผิดพลาด
            "Title": "string", // เหมืิอน "Article Name" งงจัดมาได้ไง555555
            "Article Category": "Article",
            "Published Date": "2019-06-07", //string
            "Authors List": [ // FULL: all Authors list
                "Christin Kosse",
                "Denis Burdakov"
            ],
            "Journal Link": "Nature Communications", //ไม่รู้คือไร
            "Journal Volume": "10",
            "Article Number": "2505",
            "Publication Year": "2019", // ปี publish
            "Accesses": "10k", //
            "Altmetric": "47", //
            "Abstract": "string",
            "References": [ // list of object or can be "References section not found" if no reference
                {
                    "Details": "Aggleto...data.Neuropsychologia34, 51\u201362 (1996).", // or null
                    "Article Link": "https://doi.org/10.1016%2F0028-3932%2895%2900150-6", // or null
                    "CAS Link": "/articles/cas-redirect/1:STN:280:DyaK2s%2FgsFeqtg%3D%3D", // or null
                    "Google Scholar Link": "http://scholar.google.com/scholar_lookup?&tihor=n%2CJP&author=Shaw%2CC" // or null
                },
            ],
            "Cited": [ //list of object or can be "Further reading section not found" if no cited
                {
                    "Title": "Nanobubble-actuated ultrasound neuromodulation for selectively shaping behavior in mice",
                    "Link": "https://doi.org/10.1038/s41467-024-46461-y",
                    "Authors": [
                        "Xuandi Hou",
                        "Jianing Jing",
                        "Lei Sun"
                    ],
                    "Journal Title": "Nature Communications (2024)"
                },
            ],
            "Similar Content Recommendations": [ // [] if no similar content
                {
                    "Title": "A hypothalamic novelty signal modulates hippocampal memory",
                    "Link": "https://www.nature.com/articles/s41586-020-2771-1?fromPaywallRec=false"
                }
            ]
        }
    },
