const listContainer = document.getElementById("pokemon-list");
const modal = new bootstrap.Modal(document.getElementById("pokemonModal"));

async function loadPokemons() {
  const res = await fetch("https://pokeapi.co/api/v2/pokemon?limit=12");
  const data = await res.json();

  data.results.forEach((pokemon) => {
    const col = document.createElement("div");
    col.className = "col-md-3 mb-4";
    col.innerHTML = `
      <div class="card pokemon-card shadow-sm" data-url="${pokemon.url}">
        <div class="card-body text-center">
          <h5 class="card-title text-capitalize">${pokemon.name}</h5>
        </div>
      </div>
    `;
    col.querySelector(".pokemon-card").addEventListener("click", () => showPokemon(pokemon.url));
    listContainer.appendChild(col);
  });
}

async function showPokemon(url) {
  const res = await fetch(url);
  const data = await res.json();

  document.getElementById("pokemonName").innerText = data.name.toUpperCase();
  document.getElementById("pokemonImage").src = data.sprites.front_default;
  document.getElementById("pokemonTypes").innerText = data.types.map(t => t.type.name).join(", ");
  document.getElementById("pokemonAbilities").innerText = data.abilities.map(a => a.ability.name).join(", ");

  modal.show();
}

loadPokemons();
