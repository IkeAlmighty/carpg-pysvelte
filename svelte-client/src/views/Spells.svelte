<script>
  import { onMount } from "svelte";
  import ErrorBox from "../components/ErrorBox.svelte";
  import { fetchTags, fetchSpells } from "../utilities/endpoints";
  import { spells, spelltags } from '../stores';

  let loadingMessage = "click generate to generate spells";
  let limit = 100;
  let availableTags = [];
  let selectedTag = undefined;

  onMount(() => {
    fetchTags("Spells")
      .then((res) => {
        availableTags = res.data;
      })
      .catch((error) => {
        console.log(error);
      });
  });

  const generateSpells = async (e) => {
    e.preventDefault();
    loadingMessage = "Loading...";
    $spells = []
    fetchSpells(limit, $spelltags)
      .then((res) => {
        $spells = [... res.data];
        loadingMessage = undefined;
      })
      .catch((error) => {
        loadingMessage = "Error Occured";
      });
  };

  const addSelectedTag = () => {
    if (selectedTag === "any") {
      $spelltags = [];
    } else if ($spelltags.includes("any")) {
      $spelltags.splice($spelltags.indexOf("any"), 1);
      $spelltags = [...$spelltags];
    } else if ($spelltags.includes(selectedTag)) {
      return;
    }
    $spelltags.push(selectedTag);
    $spelltags = [...$spelltags];
  };

  const removeTag = (tag) => {
    if ($spelltags.includes(tag)) {
      $spelltags.splice($spelltags.indexOf(tag), 1);
      $spelltags = [...$spelltags];
    }
  };

  const getSpellName = (spell) => {
    return spell[1] !== "-" ? `${spell[1]}: ` : "";
  };
</script>

<div class="container">
  <h1>Spells</h1>
  <form on:submit={generateSpells}>
    <label class="d-block">
      <input bind:value={limit} type="number" class="numberinput" />
      <span class="inputlabel">Total Spells</span>
    </label>

    <select bind:value={selectedTag}>
      <option hidden selected>Select Tag</option>
      {#each availableTags as tag}
        <option value={tag}>{tag.toUpperCase()}</option>
      {/each}
    </select>
    <input type="button" value="Add Tag" on:click={addSelectedTag} />
    <input type="submit" value="Generate" class="d-block" />
  </form>

  <ul>
    {#each $spelltags as tag}
      <li>
        <button
          on:click={() => {
            removeTag(tag);
          }}>{tag} (delete)</button
        >
      </li>
    {/each}
  </ul>

  Spells:
  <div class="d-block">
    <div >
      {#if $spells.length > 0}
        {#each $spells as spell}
          <div class="spellframe">
            <strong>{getSpellName(spell)}</strong>{spell[0]}
          </div>
        {/each}
      {:else if loadingMessage}
        {loadingMessage}
      {/if}
    </div>
  </div>
</div>

<style>
  .numberinput {
    width: 100px;
  }

  .spellframe {
    width: 100%;
    text-justify: distribute;
    display: block;
    margin: 2em 0;
  }

  .inputlabel {
    margin-left: 10px;
  }
</style>
