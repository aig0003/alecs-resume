from flask import Flask, render_template, url_for, redirect
import requests

app = Flask(__name__)

resume = {
	"name":"ALEC GOODNER",
	"bio":"Developer with a formal foundation in software engineering and a diverse technical skill set. Committed to learning and growing along with my peers, whether through teaching, coding, art, or other innovative avenues.",
	"contacts": {
		"email":"alec.goodner@gmail.com",
		"phone":"(404) 771-7074",
		"city":"Madison, AL",
		"linkedin":"linkedin.com/in/aig0003"
	},
	"careers": [
		{
			"company":"Xapiens International Group",
			"location": "Guaynabo, PR (Remote)",
			"title": "Jr. Software Developer",
			"dates": "June 2022 - Present",
			"description": "I handled a wide range of responsibilities, performing security and audit certification services for a wide range of clients. I would develop and employ a variety of tools and techniques to perform requested tasks, such as: creating scripts and queries to read, convert and obtain data from a large database and large client user reports, utilize AI tools to debug and navigate communication barriers with a primarily Spanish-speaking clientelle, and perform a variety of database maintenance and validation tasks to ensure that the client information was handled in a very precise and secure manner."
		},
		{
			"company":"CodeWizardsHQ",
			"location":"Austin, TX (Remote)",
			"title": "Curriculum Instructor",
			"dates":"June 2020 - April 2022",
			"description":"My role was to study, teach, and aid in the development of a full-stack computer programming curriculum aimed to educate children from K-12 levels through live, online courses. I coordinated remotely with several teams to the develop new courses and curriculum materials, provided virtual but high-quality education and feedback to students, and generally assisted the company and fellow instructors.",
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
		"SOFTWARE": [
			"MacOS, Windows 7/10, Linux",
			"Git/Github",
			"Microsoft & LibreOffice Suite",
			"Google Drive (Docs, Sheets, Slides, Forms)",
			"Adobe Photoshop & Illustrator",
			"Magento 1.9",
			"Mailchimp",
			"Slack",
			"Shortcut, Basecamp"
		],
		"LANGUAGES": [
			"Python (Flask)",
			"MySQL, SQLite3",
			"PHP/Perl",
			"HTML5, CSS3 (Bootstrap 5)",
			"JavaScript (Node, React, jQuery)",
			"AFRAME",
			"Java",
			"C++"
		],
		"OTHER": [
			"Computer Game Design (Unity3D, Godot 4)",
			"3D Printing & Modeling (TinkerCAD, Blender)",
			"Graphic Design (Photoshop, GIMP)",
			"Misc. Raspberry Pi Projects",
			"Plex Media Server",
			"Tabletop Game Design (TTRPGS, Card & Board Games)",
			"Music Production (Garageband, Logic Pro X, Audacity)",
			"Online Streaming"
		]
	}
}

@app.route("/")
def home():
	try:
		affirmation = requests.get("https://www.affirmations.dev/").json()["affirmation"]
	except:
		affirmation = "Be the person your dog thinks you are." 
	return render_template("index.html", resume=resume, affirmation=affirmation)