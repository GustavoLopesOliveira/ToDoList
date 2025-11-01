const number = document.getElementsByClassName('id')
const name = document.getElementsByClassName('name')
const description = document.getElementsByClassName('description')
const submit  = document.getElementsByClassName('submit_input') 

read()

async function read() {
    const response = await fetch("/") 
    const data = await response.json()

    const container = document.getElementsByClassName('task-list')[0] 

    container.innerHTML = ""

    data.forEach(task => {
        const div = document.createElement('div')
        div.classList.add('task')

        const idElem = document.createElement('p')
        idElem.textContent = `ID: ${task.id}`

        const nameElem = document.createElement('h3')
        nameElem.textContent = task.name

        const descElem = document.createElement('p')
        descElem.textContent = task.description

        div.appendChild(idElem)
        div.appendChild(nameElem)
        div.appendChild(descElem)

        container.appendChild(div)
    })
}
