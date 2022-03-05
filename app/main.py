from flask import Flask, render_template, url_for, redirect
import requests

app = Flask(__name__)

resume = {
	"name":"Alec Goodner",
	"bio":"Well-rounded & motivated to grow. I’ve had experience in higher education, logistics management, marketing, design, computer programming, education, and more. I aim to elevate myself as well as my peers with effective communication & teamwork.",
	"contacts": {
		"email":"alec.goodner@gmail.com",
		"phone":"404-771-7074",
		"city":"Franklin, TN",
		"linkedin":"linkedin.com/in/aig0003"
	},
	"careers": [
		{
			"company":"CodeWizardsHQ",
			"location":"Austin, TX (Fully Remote)",
			"title": "Curriculum Instructor",
			"dates":"June 2020 - Present",
			"description":"My role is to study, teach, and assist in developing a full-stack computer programming curriculum aimed to educate children from elementary to high school levels through live, online courses. I coordinate remotely with several teams to the develop new curriculum, provide quality education to students, and grow alongside with fellow instructors.",
		},
		{
			"company":"Tiger Rags Inc",
			"location":"Auburn, AL",
			"title":"eCommerce Manager",
			"dates":"July 2019 - January 2020",
			"description":"I personally and remotely communicated with various company departments, staff, and customers to ensure success in company projects. General responsibilities included managing the company online store, product catalogs, optimizing/updating social media pages, designing advertising campaigns, handling customer service, as well as tracking merchandise logistics and shipping products."
		}
	],
	"otherwork":[
		{
			"company":"Crumbl Cookies",
			"location":"Murfreesboro, TN",
			"title": "Delivery Driver/Baker",
			"dates":"November 2020 - May 2021",
			"description":"Responsibilities included aiding in the creation of company food products, logistical organization, diligently adhering to health codes and cleanliness guidelines, as well as managing GPS systems to safely and efficiently transport products to customers in a timely manner.",
		},
		{
			"company":"DoorDash Inc.",
			"location":"Auburn, AL (Varies)",
			"title": "Delivery Driver",
			"dates":"",
			"description":"",
		},
		{
			"company":"Advantage Sales & Marketing LLC",
			"location":"Auburn, AL",
			"title": "Event Specialist",
			"dates":"",
			"description":"",
		},
		{
			"company":"City of Foley",
			"location":"Foley, AL",
			"title": "Sports Complex Concessions",
			"dates":"",
			"description":"",
		},
	],
	"education": [
		{
			"degree":"Bachelor's Degree of Software Engineering (BSWE)",
			"graduationdate":"May 2019",
			"schoolname":"Auburn University",
			"schooladdress":"152 S College St, Auburn, AL 36849",
			"schoolphone":"334-844-4000"
		},
		{
			"degree":"High School AP Diploma",
			"graduationdate":"May 2015",
			"schoolname":"Foley High School",
			"schooladdress":"1 Pride Place, Foley, AL 36535",
			"schoolphone":"251-943-2221"
		}
	],
	"skills": {
		"Computer Systems": [
			"MacOS, Windows 7/10, Linux",
			"Microsoft Office Suite",
			"Google Drive (Docs, Sheets, Slides, Forms)",
			"Adobe Photoshop & Illustrator",
			"Magento 1.9",
			"Mailchimp",
			"Git/Github",
			"Slack",
			"Basecamp"
		],
		"Programming Languages": [
			"Python (Flask)",
			"HTML5, CSS3 (Bootstrap 5)",
			"JavaScript (jQuery)",
			"MySQL, SQLite3",
			"AFRAME",
			"Java",
			"C++"
		],
		"Other Experiences": [
			"3D Printing & Modeling (TinkerCAD, Google SketchUp)",
			"Graphic Design",
			"Raspberry Pi",
			"Plex Media Server",
			"Game Design (Tabletop, Cards, Video Games)",
			"Music Production (Garageband, Logic Pro X)",
			"Online Streaming"
		]
	}
}

@app.route("/")
def home():
	try:
		affirmation = requests.get("https://www.affirmations.dev/").json()["affirmation"]
	except:
		affirmation = "Be the person your dog thinks you are" 
	return render_template("index.html", resume=resume, affirmation=affirmation)