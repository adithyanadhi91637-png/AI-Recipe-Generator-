function addIngredient(item){

    let input = document.getElementById("ingredients");

    if(input.value.trim()===""){

        input.value=item.toLowerCase();

    }else{

        let list=input.value.split(",").map(i=>i.trim().toLowerCase());

        if(!list.includes(item.toLowerCase())){

            input.value += ", " + item.toLowerCase();

        }

    }

}

const hiddenElements = document.querySelectorAll(".hidden");

const observer = new IntersectionObserver((entries)=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.classList.add("show");

        }

    });

});

hiddenElements.forEach((el)=>observer.observe(el));






const counters = document.querySelectorAll(".counter");

const counterObserver = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            const counter = entry.target;
            const target = Number(counter.dataset.target);

            let current = 0;

            const updateCounter = () => {

                const increment = Math.ceil(target / 60);

                if (current < target) {

                    current += increment;

                    if (current > target) current = target;

                    counter.textContent = current + "+";

                    requestAnimationFrame(updateCounter);

                } else {

                    counter.textContent = target + "+";

                }

            };

            updateCounter();

            counterObserver.unobserve(counter);

        }

    });

});

counters.forEach(counter => counterObserver.observe(counter));