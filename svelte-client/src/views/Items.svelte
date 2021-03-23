<script>
  import axios from "axios";

  const API_URI = "http://localhost:5000/api";

  let items = [["Click 'Generate' to generate Items"]];
  let limit = 10;
  let spellchance = 100;

  const generateItems = async (e) => {
    e.preventDefault();
    items = []
    let res = await axios.get(
      `${API_URI}/items?limit=${limit}&spellchance=${spellchance}`
    );
    items = res.data;
  };
</script>

<div>
  <form on:submit={generateItems}>
    <label class="d-block">
      <input bind:value={limit} type="number" class="numberinput" /> 
      Total Items
    </label>
    <label class="d-block">
      <input bind:value={spellchance} type="number" class="numberinput" /> 
      % SpellChance
    </label>
    <input type="submit" value="Generate" class="d-block" />
  </form>
  Items:
  <div class="d-block">
    <ol class="itemframe">
      {#if items.length > 0}
      {#each items as item}
        <li>
          <strong>{item[0]}</strong>
          <div class="d-block text-small">
            Description/Action: {item[1]}
          </div>
          <div class="d-block text-small">
            {item[2]} lbs
          </div>
          <div class="d-block text-small">
            {#if item[3]}
              <strong>Spell:</strong> {item[3][0]}
            {/if}
          </div>
        </li>
      {/each}
      {:else}
        Loading...
      {/if}
    </ol>
  </div>
</div>

<style>
  .numberinput {
    width: 75px;
  }

  .itemframe {
    width: 250px;
    text-justify: distribute;
  }
</style>
