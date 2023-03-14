console.log('generate print js file connected')

function showForm() {
    var selection = document.details.version.value
    var pcp = document.getElementById('pcp')
    var mental = document.getElementById('mental')
    if(selection == 'pcp') {
        if(mental.style.display === 'flex') {
            mental.style.display = 'none'
            pcp.style.display = 'flex'
            pcp.style.flexDirection = 'column'
        } else {
            pcp.style.display = 'flex'
            pcp.style.flexDirection = 'column'
        }
    } else {
        if(pcp.style.display === 'flex') {
            pcp.style.display = 'none'
            mental.style.display = 'flex'
            mental.style.flexDirection = 'column'
        } else {
            mental.style.display = 'flex'
            mental.style.flexDirection = 'column'
        }
    }
}

async function pcpData() {
    var theUser = document.pcp.theUser.value
    var numWeeks = document.pcp.numWeeks.value

    // var response = await fetch(`https://healthLog.opencolumbiaco.org/json/${theUser}/pcpData/`)
    var response = await fetch(`http://127.0.0.1:8000/json/${theUser}/pcpData/`)
    var data = await response.json()
    console.log('all the data', data)

    if(data.weeks.length == 0){
        alert('You have no data to print')
        return
    }
    if(numWeeks > data.weeks.length) {
        alert("Lowering the number of weeks to match your logs")
    }

    var user = data.user
    var theWeeks = data.weeks
    var logs = data.logs
    var moods = data.moods
    var taken = data.takens
    var sugars = data.sugars
    var meds = data.medications
    var symptoms = data.symptoms

    var node = document.createElement('div')
    node.setAttribute('class', 'column')

    var weeks = []
    if(numWeeks > theWeeks.length) {
        for(i = 0; i < theWeeks.length; i++) {
            weeks.push(theWeeks[i])
        }
    }
    else {
        for(i=0; i< numWeeks; i++) {
            weeks.push(theWeeks[i])
        }    
    }
    for(a = 0; a < weeks.length; a++) {
        var div = document.createElement('div')
        div.setAttribute('class', 'newColumn')
        div.setAttribute('class', 'weekData')
        var h2week = document.createElement('h2')
        var h2Text = document.createTextNode(weeks[a].title)
        h2week.appendChild(h2Text)
        div.appendChild(h2week)
        for(b = 0; b < logs.length; b++) {
            if(logs[b].week_id == weeks[a].id) {
                var h3log = document.createElement('h3')
                var h3text = document.createTextNode(logs[b].day + ' - ' + logs[b].title)
                h3log.appendChild(h3text)
                div.appendChild(h3log)
                var h4Mood = document.createElement('h4')
                var h4MoodText = document.createTextNode('Moods / Symptoms Logged')
                h4Mood.appendChild(h4MoodText)
                div.appendChild(h4Mood)
                var tableMood = document.createElement('table')
                var trMood = document.createElement('tr')
                var thMood01 = document.createElement('th')
                var thMood02 = document.createElement('th')
                var thMood03 = document.createElement('th')
                var thMoodText01 = document.createTextNode('Date & Title')
                var thMoodText02 = document.createTextNode('Mood/4')
                var thMoodText03 = document.createTextNode('Symptom')
                thMood01.appendChild(thMoodText01)
                trMood.appendChild(thMood01)
                thMood02.appendChild(thMoodText02)
                trMood.appendChild(thMood02)
                thMood03.appendChild(thMoodText03)
                trMood.appendChild(thMood03)
                tableMood.appendChild(trMood)
                div.appendChild(tableMood)
                for(c = 0; c < moods.length; c++) {
                    if(moods[c].log_id == logs[b].id) {
                        var forTrMood = document.createElement('tr')
                        forTdMood01 = document.createElement('td')
                        forTdMood02 = document.createElement('td')
                        forTdMood03 = document.createElement('td')
                        forTdText01 = document.createTextNode(moods[c].date + ' ' + moods[c].tag)
                        forTdText02 = document.createTextNode(moods[c].mood + '/4')
                        forTdMood01.appendChild(forTdText01)
                        forTrMood.appendChild(forTdMood01)
                        forTdMood02.appendChild(forTdText02)
                        forTrMood.appendChild(forTdMood02)
                        tableMood.appendChild(forTrMood)
                        div.appendChild(tableMood)
                        for(d = 0; d < symptoms.length; d++) {
                            if(symptoms[d].id == moods[c].symptom_id) {
                                forTdText03 = document.createTextNode(symptoms[d].symptom)
                                forTdMood03.appendChild(forTdText03)
                                forTrMood.appendChild(forTdMood03)
                                tableMood.appendChild(forTrMood)
                                div.appendChild(tableMood)
                            }
                        }
                    }
                }
                var h4meds = document.createElement('h4')
                var h4MedsText = document.createTextNode('Medications Logged')
                h4meds.appendChild(h4MedsText)
                div.appendChild(h4meds)
                var tableMed = document.createElement('table')
                var trMed = document.createElement('tr')
                var thMed01 = document.createElement('th')
                var thMed02 = document.createElement('th')
                var thMed03 = document.createElement('th')
                var thMedText01 = document.createTextNode('Time')
                var thMedText02 = document.createTextNode('Dose')
                var thMedText03 = document.createTextNode('Medication')
                thMed01.appendChild(thMedText01)
                trMed.appendChild(thMed01)
                thMed02.appendChild(thMedText02)
                trMed.appendChild(thMed02)
                thMed03.appendChild(thMedText03)
                trMed.appendChild(thMed03)
                tableMed.appendChild(trMed)
                div.appendChild(tableMed)
                for(e = 0; e < taken.length; e++) {
                    if(taken[e].day_id == logs[b].id) {
                        var forTrMed = document.createElement('tr')
                        var forTdMed01 = document.createElement('td')
                        var forTdMed02 = document.createElement('td')
                        var forTdMed03 = document.createElement('td')
                        var forTdMedText01 = document.createTextNode(taken[e].when)
                        var forTdMedText02 = document.createTextNode(taken[e].dose)
                        forTdMed01.appendChild(forTdMedText01)
                        forTdMed02.appendChild(forTdMedText02)
                        forTrMed.appendChild(forTdMed01)
                        forTrMed.appendChild(forTdMed02)
                        tableMed.appendChild(forTrMed)
                        div.appendChild(tableMed)
                        for(f = 0; f < meds.length; f++) {
                            if(meds[f].id == taken[e].medication_id) {
                                var forTdMedText03 = document.createTextNode(meds[f].name)
                                forTdMed03.appendChild(forTdMedText03)
                                forTrMed.appendChild(forTdMed03)
                                tableMed.appendChild(forTrMed)
                                div.appendChild(tableMed)
                            }
                        }
                    }
                }
                if(user[0].level == 1) {
                    var h4Sugar = document.createElement('h4')
                    var h4SugarText = document.createTextNode("Sugar Readings Logged")
                    h4Sugar.appendChild(h4SugarText)
                    div.appendChild(h4Sugar)
                    var tableSugar = document.createElement('table')
                    var trSugar = document.createElement('tr')
                    var thSugar01 = document.createElement('th')
                    var thSugar02 = document.createElement('th')
                    var thSugarText01 = document.createTextNode('When')
                    var thSugarText02 = document.createTextNode('Reading')
                    thSugar01.appendChild(thSugarText01)
                    trSugar.appendChild(thSugar01)
                    thSugar02.appendChild(thSugarText02)
                    trSugar.appendChild(thSugar02)
                    tableSugar.appendChild(trSugar)
                    div.appendChild(tableSugar)
                    for(g = 0; g < sugars.length; g++) {
                        if(sugars[g].note_id == logs[b].id) {
                            var forTrSugar = document.createElement('tr')
                            var forTdSugar01 = document.createElement('td')
                            var forTdSugar02 = document.createElement('td')
                            var forTdSugarText01 = document.createTextNode(sugars[g].time)
                            var forTdSugarText02 = document.createTextNode(sugars[g].level)
                            forTdSugar01.appendChild(forTdSugarText01)
                            forTrSugar.appendChild(forTdSugar01)
                            forTdSugar02.appendChild(forTdSugarText02)
                            forTrSugar.appendChild(forTdSugar02)
                            tableSugar.appendChild(forTrSugar)
                            div.appendChild(tableSugar)
                        }
                    }
                }
            }
        }
        node.appendChild(div)
        document.getElementById('print').appendChild(node)
    }
}

async function mentalData() {
    var theUser = document.mental.theUser.value
    var numWeeks = document.mental.numWeeks.value 
    // var response = await fetch(`https://healthLog.opencolumbiaco.org/json/${theUser}/mentalData/`)
    var response = await fetch(`http://127.0.0.1:8000/json/${theUser}/mentalData/`)
    var data = await response.json()
    console.log('all the data', data)

    if(data.weeks.length == 0){
        alert('You have no data to print')
        return
    }
    if(numWeeks > data.weeks.length) {
        alert("Lowering the number of weeks to match your logs")
    }

    var user = data.user
    var theWeeks = data.weeks
    var logs = data.logs
    var moods = data.moods
    var meds = data.medications
    var symptoms = data.symptoms

    var node = document.createElement('div')
    node.setAttribute('class', 'column')

    var weeks = []
    if(numWeeks > theWeeks.length) {
        for(i = 0; i < theWeeks.length; i++) {
            weeks.push(theWeeks[i])
        }
    }
    else {
        for(i=0; i< numWeeks; i++) {
            weeks.push(theWeeks[i])
        }    
    }

    for(a = 0; a < weeks.length; a++) {
        var div = document.createElement('div')
        div.setAttribute('class', 'newColumn')
        div.setAttribute('class', 'weekData')
        var h2week = document.createElement('h2')
        var h2Text = document.createTextNode(weeks[a].title)
        h2week.appendChild(h2Text)
        div.appendChild(h2week)
        for(b = 0; b < logs.length; b++) {
            if(logs[b].week_id == weeks[a].id) {
                var h3log = document.createElement('h3')
                var h3text = document.createTextNode(logs[b].day + ' - ' + logs[b].title)
                h3log.appendChild(h3text)
                div.appendChild(h3log)
                var h4Mood = document.createElement('h4')
                var h4MoodText = document.createTextNode('Moods / Symptoms Logged')
                h4Mood.appendChild(h4MoodText)
                div.appendChild(h4Mood)
                var tableMood = document.createElement('table')
                var trMood = document.createElement('tr')
                var thMood01 = document.createElement('th')
                var thMood02 = document.createElement('th')
                var thMood03 = document.createElement('th')
                var thMoodText01 = document.createTextNode('Date & Title')
                var thMoodText02 = document.createTextNode('Mood/4')
                var thMoodText03 = document.createTextNode('Symptom')
                thMood01.appendChild(thMoodText01)
                trMood.appendChild(thMood01)
                thMood02.appendChild(thMoodText02)
                trMood.appendChild(thMood02)
                thMood03.appendChild(thMoodText03)
                trMood.appendChild(thMood03)
                tableMood.appendChild(trMood)
                div.appendChild(tableMood)
                for(c = 0; c < moods.length; c++) {
                    if(moods[c].log_id == logs[b].id) {
                        var forTrMood = document.createElement('tr')
                        forTdMood01 = document.createElement('td')
                        forTdMood02 = document.createElement('td')
                        forTdMood03 = document.createElement('td')
                        forTdText01 = document.createTextNode(moods[c].date + ' ' + moods[c].tag)
                        forTdText02 = document.createTextNode(moods[c].mood + '/4')
                        forTdMood01.appendChild(forTdText01)
                        forTrMood.appendChild(forTdMood01)
                        forTdMood02.appendChild(forTdText02)
                        forTrMood.appendChild(forTdMood02)
                        tableMood.appendChild(forTrMood)
                        div.appendChild(tableMood)
                        for(d = 0; d < symptoms.length; d++) {
                            if(symptoms[d].id == moods[c].symptom_id) {
                                forTdText03 = document.createTextNode(symptoms[d].symptom)
                                forTdMood03.appendChild(forTdText03)
                                forTrMood.appendChild(forTdMood03)
                                tableMood.appendChild(forTrMood)
                                div.appendChild(tableMood)
                            }
                        }
                    }
                }
                var contentTable = document.createElement('table')
                var contentHeadRow = document.createElement('tr')
                var contentRow = document.createElement('tr')
                var contentHeader = document.createElement('th')
                var contentHeadText = document.createTextNode('Notes Taken')
                contentHeader.appendChild(contentHeadText)
                contentHeadRow.appendChild(contentHeader)
                contentTable.appendChild(contentHeadRow)
                var contentData = document.createElement('td')
                var pText = document.createTextNode(logs[b].content)
                contentData.appendChild(pText)
                contentRow.appendChild(contentData)
                contentTable.appendChild(contentRow)
                div.appendChild(contentTable)

            }
        }
        node.appendChild(div)
        document.getElementById('print').appendChild(node)
    }
}

var doc = new jsPDF();
var specialElementHandlers = {
    '#editor': function (element, renderer) {
        return true;
    }
};

$('#printButton').click(function () {
    doc.fromHTML($('#print').html(), 15, 15, {
        'width': 800,
        'elementHandlers': specialElementHandlers
    });
    doc.save('healthLogData.pdf');
});