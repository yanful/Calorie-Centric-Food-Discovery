import urllib.request, urllib.error, urllib.parse, json, webbrowser
import requests

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

def safe_get(url):
    try:
        return urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print("The server couldn't fulfill the request." )
        print("Error code: ", e.code)
    except urllib.error.URLError as e:
        print("We failed to reach a server")
        print("Reason: ", e.reason)
    return None

#key = "62282f9a4c7f49e7add369173314bc91"
baseurl1 = "https://api.spoonacular.com/recipes/findByNutrients"
def get_food_plan(apiKey = "62282f9a4c7f49e7add369173314bc91", includeNurtrition = True, minCalories=None, maxCalories=None, number=10):
    parameters = {"apiKey": apiKey,"minCalories": minCalories,
                  "includeNurtrition": includeNurtrition,
                  "maxCalories": maxCalories, "number": number}
    headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
    response = requests.get(baseurl1, params=parameters, headers=headers)
    pages_print = json.loads(response.text)
    return pages_print
plan = get_food_plan(minCalories=600, maxCalories=800, number=2)
print(pretty(plan))

def get_food_carbohydrates(apiKey = "62282f9a4c7f49e7add369173314bc91", includeNurtrition = True, minCarbs=None, maxCarbs=None, number=10):
    parameters = {"apiKey": apiKey,"minCarbs": minCarbs,
                  "includeNurtrition": includeNurtrition,
                  "maxCarbs": maxCarbs, "number": number}
    headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
    response = requests.get(baseurl1, params=parameters, headers=headers)
    pages_print = json.loads(response.text)
    return pages_print
plan3 = get_food_carbohydrates(minCarbs=100, maxCarbs=300, number=2)
print(pretty(plan3))

def get_food_fat(apiKey = "62282f9a4c7f49e7add369173314bc91", includeNurtrition = True, minFat=None, maxFat=None, number=10):
    parameters = {"apiKey": apiKey,"minFat": minFat,
                  "includeNurtrition": includeNurtrition,
                  "maxFat": maxFat, "number": number}
    headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
    response = requests.get(baseurl1, params=parameters, headers=headers)
    pages_print = json.loads(response.text)
    return pages_print
plan4 = get_food_fat(minFat=30, maxFat=100, number=2)
print(pretty(plan4))

baseurl2 = "https://api.spoonacular.com/recipes/quickAnswer"
def get_search_result(apiKey = "62282f9a4c7f49e7add369173314bc91", includeNurtrition = True, q = None):
    parameters = {"apiKey": apiKey,
                  "includeNurtrition": includeNurtrition,
                  "q": q}
    headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
    response = requests.get(baseurl2, params=parameters, headers=headers)
    pages_print = json.loads(response.text)
    return pages_print
plan2 = get_search_result(q = "How much vitamin c is in 2 apples")
print(pretty(plan2))


class Food():
    def __init__(self, list):
        self.calories = list["calories"]
        self.fat = list["fat"]
        self.carbs = list["carbs"]
        self.id = list["id"]
        self.title = list["title"]
        self.image = list["image"]

    def make_photo_url(self):
        return self.image
        # return "https://spoonacular.com/recipes/{id}/ingredientWidget.png".format(id=self.id)

    def food_name(self):
        return self.title

    def __str__(self):
        return "title: " + str(self.title) + "\n" + "id: " + str(self.id) + "\n" + "carbs: " + str(self.carbs) + "\n" + "calories: " + str(self.calories) + "\n" + "fat: " + str(self.fat) + "\n" + "image: " + str(self.image)



def sort_list(plan):
    wholelist = []
    for item in plan:
        wholelist.append(Food(item))
    return sorted(wholelist, key=lambda num_calories: num_calories.calories, reverse=False)

def sort_list2(plan):
    wholelist = []
    for item in plan:
        wholelist.append(Food(item))
    return sorted(wholelist, key=lambda num_carbohydrates: num_carbohydrates.carbs, reverse=False)

def sort_list3(plan):
    wholelist = []
    for item in plan:
        wholelist.append(Food(item))
    return sorted(wholelist, key=lambda num_fat: num_fat.fat, reverse=False)

def result_list(plan2):
    return plan2["answer"]


# new_dic = {"wholelist": wholelist}
# import jinja2, os
#
# JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'], autoescape=True)
# template = JINJA_ENVIRONMENT.get_template('templates/projecttemplate.html')
# with open('templates/flask_page.html', 'w') as webpagefile:
#     webpagefile.write(template.render(new_dic))

# def flickrREST(baseurl = 'https://api.spoonacular.com/recipes/findByNutrients',
#     apiKey = key,
#     format ='json',
#     params={},
#     includeNutrition = True,
#     ):
#     params['apiKey'] = apiKey
#     params["includeNurtrition"] = includeNutrition
#     params['format'] = format
#     if format == "json": params["nojsoncallback"]=True
#     url = baseurl + "?" + urllib.parse.urlencode(params)
#     if includeNutrition:
#         print(url)
#     return safe_get(url)


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main_handler():
    app.logger.info("In MainHandler")
    return render_template('flask_page.html')

@app.route("/gresponse", methods =["GET", "POST"])
def gfg():
    app.logger.info(request.form.get('search_foodplan_min'))
    app.logger.info(request.form.get('search_foodplan_max'))
    min_value = request.form.get('search_foodplan_min')
    max_value = request.form.get("search_foodplan_max")
    if min_value and max_value:
        food_json = get_food_plan(minCalories=min_value, maxCalories=max_value)
        x = sort_list(food_json)
        if min_value <= max_value:
            return render_template('response.html', x=x)
        elif min_value > max_value:
            return render_template('flask_page.html', prompt="Please enter the correct value.")
    else:
        return render_template('flask_page.html', prompt="Please try again")


@app.route("/gr", methods =["GET", "POST"])
def result():
    app.logger.info(request.form.get('search_result'))
    search_for_result = request.form.get('search_result')
    if search_for_result:
        if get_search_result(q=search_for_result):
            results = get_search_result(q=search_for_result)
            final_list = result_list(results)
            if results:
                return render_template('flask_page.html', theanswer=final_list)
        else:
            return render_template('flask_page.html', theanswer="Sorry, we don't have answer for you")
    else:
        return render_template('flask_page.html', theanswer="Sorry, we don't have answer for you")

@app.route("/gc", methods =["GET", "POST"])
def gcg():
    app.logger.info(request.form.get('search_carbohydrates_min'))
    app.logger.info(request.form.get('search_carbohydrates_max'))
    min_value = request.form.get("search_carbohydrates_min")
    max_value = request.form.get("search_carbohydrates_max")
    if min_value and max_value:
        food_json = get_food_carbohydrates(minCarbs=min_value, maxCarbs=max_value)
        x = sort_list2(food_json)
        if min_value <= max_value:
            return render_template('response.html', x=x)
        elif min_value > max_value:
            return render_template('flask_page.html', carbohydrates="Please enter the correct value.")
    else:
        return render_template('flask_page.html', carbohydrates="Please try again")

@app.route("/gf", methods =["GET", "POST"])
def gcf():
    app.logger.info(request.form.get('search_fat_min'))
    app.logger.info(request.form.get('search_fat_max'))
    min_value = request.form.get("search_fat_min")
    max_value = request.form.get("search_fat_max")
    if min_value and max_value:
        food_json = get_food_fat(minFat=min_value, maxFat=max_value)
        x = sort_list3(food_json)
        if min_value <= max_value:
            return render_template('response.html', x=x)
        elif min_value > max_value:
            return render_template('flask_page.html', fat="Please enter the correct value.")
    else:
        return render_template('flask_page.html', fat="Please try again")

if __name__=='__main__':
   app.run(host="localhost", port=8080, debug=True)

# comment: Spoonacular api sign up - https://spoonacular.com/food-api/console#Dashboard