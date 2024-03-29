from flask import Flask, render_template, url_for, redirect
import requests

app = Flask(__name__)

# Could be a JSON file
resume = {
	"name":"ALEC GOODNER",
	"bio":"\"A Developer with a Bachelor’s in Software Engineering and experience in Python, MySQL, Java, and JavaScript among others as a jr. software developer and educational instructor. Skilled in programming, data management, scripting, and experiences in bilingual communication. Committed to continuous learning and growth through a variety of outlets and fields.\"",
	"contacts": {
		"linkedin-link":"linkedin.com/in/aig0003",
		"github-link":"github.com/aig0003",
		"email":"alec.goodner@gmail.com",
		"phone":"(404) 771-7074",
		"city":"Madison, AL"
	},
	"careers": [
		{
			"company":"Xapiens International Group",
			"location": "Guaynabo, PR (Remote)",
			"title": "Jr. Software Developer",
			"dates": "June 2022 - Present",
	   	 	"description": [
	   			 "Would validate and convert application user reports into audit certification campaigns, which would ensure clients audits were passed with accurate data in a timely manner.",
	   			 "Managed and navigated large data databases, Primarily MySQL, including hundreds of tables, and millions of entries to generate various user, certification, and network log reports, update and maintain client account and application information.",
	   			 "Created various custom scripts to validate/handle report data, document activities done, and perform other miscellaneous features. Often using Bash, PHP and Python.",
	   			 "Remotely communicated with various clients and team members across language barriers, with many employees and clientes speaking Spanish primarily, to ensure requests were fulfilled accurately, often using various translation and AI tools to ensure effective communications."
	   		 ]
	   			 #"description": "I handled a wide range of responsibilities, performing security and audit certification services for a wide range of clients. I would develop and employ a variety of tools and techniques to perform requested tasks, such as: creating scripts and queries to read, convert and obtain data from a large database and large client user reports, utilize AI tools to debug and navigate communication barriers with a primarily Spanish-speaking clientele, and perform a variety of database maintenance and validation tasks to ensure that the client information was handled in a very precise and secure manner."
	   	 },
	   	 {
	   		 "company":"CodeWizardsHQ",
	   		 "location":"Austin, TX (Remote)",
	   		 "title": "Curriculum Instructor",
	   		 "dates":"June 2020 - April 2022",
	   		 "description":[
	   			 "Taught children from K-12 levels on full-stack concepts and programming languages through live, online courses. These courses covered a range of materials, dealing with languages such as Java, Python (+Flask), HTML/CSS/JS (+JQuery and other libraries), Scratch & SQL; as well as concepts of database management, front & back-end coding, UI design, and more.",
	   			 "Assisted in the development of new curriculum materials within tight deadline release schedules. Adhered to strict guidelines to ensure high-quality material with an emphasis on ensuring clear concepts and engaging exercises."
	   		 ]
	   		 #"description":"My role was to study, teach, and aid in the development of a full-stack computer programming curriculum aimed to educate children from K-12 levels through live, online courses. I coordinated remotely with several teams to the develop new courses and curriculum materials, provided virtual but high-quality education and feedback to students, and generally assisted the company and fellow instructors.",
	   	 },
	   	 {
	   		 "company":"Tiger Rags Inc",
	   		 "location":"Auburn, AL",
	   		 "title":"eCommerce Manager",
	   		 "dates":"July 2019 - January 2020",
	   		 "description":[    
	   			 "Maintained the store website to ensure the e-store and product catalog was up-to-date, appealing, and accurate. As well as aid in any technical issues dealing with the online tools.",
	   			 "Handled the packaging and shipping of store merchandise purchased from the online store, ensuring safe and  timely deliveries to customers.",
	   			 "Managed various social media accounts as well as create and optimize advertisement campaigns for new and existing products and specials."
	   		 ]
			#"description":"I personally and remotely communicated with various company departments, staff, and customers to ensure success in company projects. General responsibilities included managing the company online store, product catalogs, optimizing/updating social media pages, designing advertising campaigns, handling customer service, as well as tracking merchandise logistics and shipping products."
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
		}
		#,{
		#	"degree":"High School AP Diploma",
		#	"graduationdate":"May 2015",
		#	"schoolname":"Foley High School",
		#	"schooladdress":"1 Pride Place, Foley, AL 36535",
		#	"schoolphone":"251-943-2221"
		#}
	],
	"skills": {
		"SOFTWARE/TOOLS": [
			"Operating Systems: MacOS, Windows 7/10, Linux (Ubuntu)",
			"Editors/IDE's: Visual Studio, Vim, Nano, Sublime Text",
			"Version Control Software: Git/Github",
			"Document Suites: Microsoft Office, LibreOffice, Google Drive",
			"Graphic Design Applications: Adobe Photoshop & Illustrator",
			"eCommerce: Magento 1.9, Mailchimp",
			"Project Coordination: Slack, Shortcut, Basecamp"
		],
		"COMPUTER LANGUAGES": [
			"Python (Incl. Flask)",
			"MySQL, SQLite3",
			"PHP/Perl",
			"HTML5, CSS3 (Bootstrap 5)",
			"JavaScript (Incl. Node, React, jQuery)",
			"AFRAME",
			"Java",
			"C++"
		]
		#,
		#"OTHER EXPERIENCES": [
		#	"Video Game Design: Created experimental games using Unity3D and Godot 4. Learned how to use C#, GDScript, and game design principles.",
		#	"3D printing and modeling: Designed and printed various models and objects using TinkerCAD and Blender. Learned how to use 3D modeling software and hardware.",
		#	"Tabletop Game design: Designed and playtested several tabletop games, including TTRPGs, card, and board games. Learned how to create engaging systems, balanced game mechanics and narratives."
		#	"Graphic Design: Have created a variety of graphics and other artistic endeavors using Adobe Photoshop and GIMP. Learned visual design principles.",
		#	"Raspberry Pi Projects: Experimented with many projects via Raspberry Pi, inlcuding PiHole and Plex Media Servers. Learned remote accessing and server management.",
		#	"Music Production: Dabbled music creation via Garageband, Logic Pro X, and Audacity. Learned music theory and composition."
		#]
	},
	"otherexperiences": [
			{
				"title":"Video Game Design",
				"description":"Created experimental 1st & 3rd person games using Unity3D and Godot 4. Learned how to use C#, GDScript, and game design principles.",
			},
			{
				"title":"3D printing & Modeling",
				"description":"Designed and printed various models and objects using TinkerCAD, Cura, and Blender. Learned how to use 3D modeling software and hardware."
			},
			{
				"title":"Tabletop Game Design",
				"description":"Designed and playtested several tabletop games, including TTRPGs, card, and board games. Learned how to create engaging systems, balanced game mechanics and narratives."
			},
			{
				"title":"Graphic Design",
				"description":"Have created a variety of graphics and other artistic endeavors using Adobe Photoshop and GIMP. Learned visual design principles."
			},
			{
				"title":"Raspberry Pi Projects",
				"description":"Experimented with many projects via Raspberry Pi, including PiHole and Plex Media Servers. Learned remote accessing and server management."
			},
			{
				"title":"Music Production",
				"description":"Dabbled music creation via Garageband, Logic Pro X, and Audacity. Learned music theory and composition."
			}
		]
}

@app.route("/")
def home():
	try:
		affirmation = requests.get("https://www.affirmations.dev/").json()["affirmation"]
	except:
		affirmation = "Be the person your dog thinks you are." 
	return render_template("index.html", resume=resume, affirmation=affirmation)
