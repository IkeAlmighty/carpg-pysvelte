<script>
  import axios from "axios";
  import ItemCard from "../components/ItemCard.svelte";
  import { API_URI } from "../constants";

  let items = [];
  let loadingMessage = "Click 'Generate' to create a new set of items.";
  let limit = 10;
  let spellchance = 100;

  const generateItems = async (e) => {
    e.preventDefault();
    items = [];
    loadingMessage = "Loading...";
    try {
      let res = await axios.get(
        `${API_URI}/items?limit=${limit}&spellchance=${spellchance}`
      );
      items = res.data;
    } catch (error) {
      loadingMessage = "Error Occured";
    }
  };
</script>

<div class="container">
  <h1>Item Generator</h1>
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
            <ItemCard {item} />
          </li>
        {/each}
      {:else}
        {loadingMessage}
      {/if}
    </ol>
  </div>
</div>

<style>
  .numberinput {
    width: 100px;
  }

  .itemframe {
    width: 250px;
    text-justify: distribute;
  }
</style>
