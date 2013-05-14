decisions
=========

Everything you need to publish/view or recount elections and votes based on different voting systems

# Ziele

# Installation

# Datenmodell
Es wurde versucht alle Interessanten Faelle und Informationen die im Kontext von Wahlen und Abstimmungen in den verschiedenen Verfahren auftauchen in einer Datenstruktur zu speichern. Falls Fehler oder Informationen hier nicht abbildbar sind bin ich offen fuer Vorschlaege.
Hier ein proof of concept Beispiel in JSON. Die Implementierung mag sich z.B. durch IDs und/oder URLs unterscheiden

```javascript
decision:{
	"type":"Personenwahl", #Personenwahl oder Abstimmung
	"method":{
		"name":"Schulze", #Abstimmverfahrensname
		"preference":1, #TODO Hier muessen noch einstellungen der Verfahren auftauchen
	},
	"votes_count":10,
	"votes_valid":8,
	"votes":[
		{
			"ballotbox":1, #optional
			"options":[
				{
					"option_id":1,
					"value":0
				},
				{
					"option_id":2,
					"value":1
				}
			]
		}
	],
	"options":[
		{
			"id":1,
			"name":"Niels Essemvau",
		},
		{
			"id":2,
			"name":"Fritz",
			"url":"www.example.com" #optional
		}
	],
	"ballot_boxes":[#optional
		{
			"id":1,
			"name":"Urne"
		}
	]
}
```

Es fehlt: Die Speicherung des Ergebnisses sowie der Parameter fuer das angewandte Verfahren

##Zu den Stimmzetteln
Das 'value' Feld kann hier vieles ausdruecken je nachdem welches Verfahren verwendet wird.
Einige Beispiele:
* Schulze
 * Positive Werte stehen fuer ein Ja sowie die Sortierung
 * Negative Werte stehen fuer Nein mit der Sortierung
 * 0 Steht fuer Enthaltung
* Approval
 * -1 Steht fuer Nein
 * +1 Steht fuer Ja
* AV Verfahren
 * Negative Werte wie -1 ist Nein
 * Positive Werte geben direkt die Anzahl der vergebenen Punkte wieder
