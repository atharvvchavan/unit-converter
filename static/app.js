const units = JSON.parse(document.getElementById("units").textContent);

const category = document.getElementById("category");
const value = document.getElementById("value");
const fromSel = document.getElementById("from");
const toSel = document.getElementById("to");
const result = document.getElementById("result");

function fill(select, items) {
    select.innerHTML = "";
    items.forEach((item) => {
        const option = document.createElement("option");
        option.value = item;
        option.textContent = item;
        select.appendChild(option);
    });
}

async function convert() {
    if (value.value === "") {
        result.textContent = "";
        return;
    }
    const params = new URLSearchParams({
        category: category.value,
        value: value.value,
        from: fromSel.value,
        to: toSel.value,
    });
    try {
        const response = await fetch("/api/convert?" + params);
        const data = await response.json();
        result.textContent = response.ok
            ? data.value + " " + data.from_unit + " = " + data.result + " " + data.to_unit
            : data.error;
    } catch (error) {
        result.textContent = "Could not reach the server.";
    }
}

function loadUnits() {
    const list = units[category.value];
    fill(fromSel, list);
    fill(toSel, list);
    toSel.selectedIndex = Math.min(1, list.length - 1);
    convert();
}

fill(category, Object.keys(units));

category.addEventListener("change", loadUnits);
value.addEventListener("input", convert);
fromSel.addEventListener("change", convert);
toSel.addEventListener("change", convert);

document.getElementById("swap").addEventListener("click", () => {
    const oldFrom = fromSel.value;
    fromSel.value = toSel.value;
    toSel.value = oldFrom;
    convert();
});

loadUnits();