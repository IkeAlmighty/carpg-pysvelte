<script>
  import ItemCard from "../components/ItemCard.svelte";
  import { fetchItems, fetchTags } from "../utilities/endpoints";
  import { onMount } from "svelte";
  import { items, itemtags } from '../stores';

  let loadingMessage = "Click 'Generate' to create a new set of items.";
  let limit = undefined;
  let seed = undefined;
  let spellchance = undefined;
  let availableTags = [];
  let selectedTag = undefined;

  onMount(async () => {
    fetchTags("Items")
      .then((res) => {
        availableTags = res.data;
      })
      .catch((error) => {
        console.log(error);
      });
  });

  const addSelectedTag = () => {
    if (selectedTag === "any") {
      $itemtags = [];
    } else if ($itemtags.includes("any")) {
      $itemtags.splice($itemtags.indexOf("any"), 1);
      $itemtags = [...$itemtags];
    } else if ($itemtags.includes(selectedTag)) {
      return;
    }
    $itemtags.push(selectedTag);
    $itemtags = [...$itemtags];
  };

  const removeTag = (tag) => {
    if ($itemtags.includes(tag)) {
      $itemtags.splice($itemtags.indexOf(tag), 1);
      $itemtags = [...$itemtags];
    }
  };

  const generateItems = async (e) => {
    e.preventDefault();
    if(!limit) limit = 10;
    if(!spellchance) spellchance = 100;
    loadingMessage = "Loading...";
    $items = [];
    fetchItems(limit, spellchance, $itemtags, seed)
      .then((res) => {
        $items = res.data;
        loadingMessage = undefined;
        limit = undefined;
        spellchance = undefined;
      })
      .catch((error) => {
        loadingMessage = "Error Occured";
      });
  };
</script>

<div class="container">
  <h1>Item Generator</h1>
  <form on:submit={generateItems}>
    <div class="col2">
      <input bind:value={seed} type="text" class="numberinput" placeholder="Seed"/>
      <span class="inputlabel">Seed</span>

      <input bind:value={limit} type="number" class="numberinput" placeholder="Total Items"/>
      <span class="inputlabel">Total Items</span>

      <input bind:value={spellchance} type="number" class="numberinput" placeholder="Percent Spellchance"/>
      <span class="inputlabel">Spell Chance</span>
    </div>

    {#if availableTags}
      <select bind:value={selectedTag}>
        <option hidden selected>Select Tag</option>
        {#each availableTags as tag}
          <option value={tag}>{tag.toUpperCase()}</option>
        {/each}
      </select>
      <input type="button" value="Add Tag" on:click={addSelectedTag} />
    {/if}
    <input type="submit" value="Generate" class="d-block" />
  </form>

  <ul>
    {#each $itemtags as tag}
      <li>
        <button
          on:click={() => {
            removeTag(tag);
          }}>{tag} (delete)</button
        >
      </li>
    {/each}
  </ul>
  <!--  -->
  <!-- Display the Items -->
  Items ({$items.length}) :
  <div class="d-block">
    <div class="itemframe">
      {#if $items.length > 0}
        {#each $items as item}
            <ItemCard {item} />
        {/each}
      {:else if loadingMessage}
        {loadingMessage}
      {/if}
    </div>
  </div>
</div>

<style>
  form .col2 {
    display: grid;
    grid-template-columns: auto auto
  }
  .numberinput {
    width: 100%;
  }

  .inputlabel {
    padding: 0.5em;
  }

  .itemframe {
    width: 100%;
    text-justify: distribute;
  }
</style>
