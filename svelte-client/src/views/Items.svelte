<script>
  import ItemCard from "../components/ItemCard.svelte";
  import { fetchItems, fetchTags } from "../utilities/endpoints";
  import { onMount } from "svelte";
  import { items } from '../stores';

  let loadingMessage = "Click 'Generate' to create a new set of items.";
  let limit = 10;
  let seed = undefined;
  let spellchance = 100;
  let availableTags = [];
  let selectedTag = undefined;
  let tags = [];

  onMount(async () => {
    fetchTags()
      .then((res) => {
        availableTags = res.data;
      })
      .catch((error) => {
        console.log(error);
      });
  });

  const addSelectedTag = () => {
    if (selectedTag === "any") {
      tags = [];
    } else if (tags.includes("any")) {
      tags.splice(tags.indexOf("any"), 1);
      tags = [...tags];
    } else if (tags.includes(selectedTag)) {
      return;
    }
    tags.push(selectedTag);
    tags = [...tags];
  };

  const removeTag = (tag) => {
    if (tags.includes(tag)) {
      tags.splice(tags.indexOf(tag), 1);
      tags = [...tags];
    }
  };

  const generateItems = async (e) => {
    e.preventDefault();
    loadingMessage = "Loading...";
    $items = [];
    fetchItems(limit, spellchance, tags, seed)
      .then((res) => {
        $items = res.data;
        loadingMessage = undefined;
      })
      .catch((error) => {
        loadingMessage = "Error Occured";
      });
  };
</script>

<div class="container">
  <h1>Item Generator</h1>
  <form on:submit={generateItems}>
    <label class="d-block">
      <input bind:value={seed} type="text" class="numberinput" />
      <span class="inputlabel">Seed</span>
    </label>

    <label class="d-block">
      <input bind:value={limit} type="number" class="numberinput" />
      <span class="inputlabel">Total Items</span>
    </label>

    <label class="d-block">
      <input bind:value={spellchance} type="number" class="numberinput" />
      <span class="inputlabel">% SpellChance</span>
    </label>

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
    {#each tags as tag}
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
  Items:
  <div class="d-block">
    <ol class="itemframe">
      {#if $items.length > 0}
        {#each $items as item}
          <li>
            <ItemCard {item} />
          </li>
        {/each}
      {:else if loadingMessage}
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

  .inputlabel {
    margin-left: 10px;
  }
</style>
