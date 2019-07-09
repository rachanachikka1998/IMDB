from ratings.models import Actor, Movie

actors = [
    {
        "name": "sam",
        "birth_date": "1989-02-26",
        "gender": "female"

    },
    {
        "name": "deepika",
        "birth_date": "1989-03-31",
        "gender": "female"
    },
    {
        "name": "tony stark",
        "birth_date": "1979-06-12",
        "gender": "male"
    },
    {
        "name": "harry",
        "birth_date": "1969-08-21",
        "gender": "male"
    },
    {
        "name": "kate winslet",
        "birth_date": "1978-04-23",
        "gender": "female"
    },
    {
        "name": "kajal",
        "birth_date": "1988-09-15",
        "gender": "female"
    },
    {
        "name": "rajini",
        "birth_date": "1966-06-30",
        "gender": "male"
    },
    {
        "name": "sonakshi",
        "birth_date": "1985-11-30",
        "gender": "female"
    },
    {
        "name": "kangana",
        "birth_date": "1992-12-31",
        "gender": "female"
    },
    {
        "name": "siddarth",
        "birth_date": "1985-04-16",
        "gender": "male"
    }
]
movies = [

    {
        "title": "iron man",
        "release_date": "2001-05-02",
    },
    {
        "title": "queen",
        "release_date": "2006-06-12"
    },
    {
        "title": "abcd",
        "release_date": "2013-05-13"
    }
]

movie_cast = [
    {
        "movie": "iron man",
        "cast": "tony stark",
        "role": "hero"
    },
    {
        "movie": "iron man",
        "cast": "kangana",
        "role": "heroin"
    },
    {
        "movie": "iron man",
        "cast": "siddarth",
        "role": "side role"
    },
    {
        "movie": "abcd",
        "cast": "kajal",
        "role": "heroin"
    },
    {
        "movie": "abcd",
        "cast": "kate winslet",
        "role": "mom"
    },
    {
        "movie": "queen",
        "cast": "sam",
        "role": "heroin"
    }
]
ratings = [
    {
        "movie": "iron man",
        "rating": 5,
        "number": 7665
    },
    {
        "movie": "iron man",
        "rating": 4,
        "number": 4343
    },
    {
        "movie": "iron man",
        "rating": 3,
        "number": 3232
    },
    {
        "movie": "iron man",
        "rating": 2,
        "number": 432
    },
    {
        "movie": "iron man",
        "rating": 1,
        "number": 122
    },
    {
        "movie": "queen",
        "rating": 5,
        "number": 2211
    },
    {
        "movie": "queen",
        "rating": 4,
        "number": 4323
    },
    {
        "movie": "queen",
        "rating": 3,
        "number": 9234
    },
    {
        "movie": "queen",
        "rating": 2,
        "number": 234
    },
    {
        "movie": "queen",
        "rating": 1,
        "number": 123
    },
    {
        "movie": "abcd",
        "rating": 1,
        "number": 123
    },
    {
        "movie": "abcd",
        "rating": 2,
        "number": 234
    },
    {
        "movie": "abcd",
        "rating": 3,
        "number": 4354
    },
    {
        "movie": "abcd",
        "rating": 4,
        "number": 1433
    },
    {
        "movie": "abcd",
        "rating": 5,
        "number": 122
    }

]
