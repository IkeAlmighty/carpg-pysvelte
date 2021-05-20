<script>
  import CharacterCard from "../components/CharacterCard.svelte";

  import CharacterFactory from "../utilities/CharacterFactory";
  import { characters } from "../stores";

  let selectedName;
  let selectedCharacterClass = CharacterFactory.npc;
  let selectedTier;

  const createCharacter = (e) => {
    e.preventDefault();

    let name = selectedName; // reset allows us to click create multiple in a row before the first is loaded
    selectedName = undefined;

    let tier = parseInt(selectedTier) ? parseInt(selectedTier) : 5;

    selectedCharacterClass.generate(name, tier);
  };
</script>

<div class="container">
  <h1>Character Creator</h1>
  <form on:submit={createCharacter}>
    <input
      class="inputfield"
      bind:value={selectedName}
      type="text"
      placeholder="Character Name (Currently Randomized)"
    />
    {#if selectedCharacterClass === CharacterFactory.npc}
      <select class="inputfield" bind:value={selectedTier}>
        {#each [1, 2, 3, 4, 5] as tier}
          <option value={tier}>{tier}</option>
        {/each}
        <option selected hidden>Tier Level (1 being most powerful)</option>
      </select>
    {/if}

    <select class="inputfield" bind:value={selectedCharacterClass}>
      <!-- <option disable selected hidden value="">Select a Character Class</option> -->
      <option value={CharacterFactory.ancientOne}
        >{CharacterFactory.ancientOne.label}</option
      >
      <option value={CharacterFactory.militaryGrunt}
        >{CharacterFactory.militaryGrunt.label}</option
      >
      <option value={CharacterFactory.artificer}
        >{CharacterFactory.artificer.label}</option
      >
      <option value={CharacterFactory.medicHealer}
        >{CharacterFactory.medicHealer.label}</option
      >
      <option value={CharacterFactory.diplomatLinguist}
        >{CharacterFactory.diplomatLinguist.label}</option
      >
      <option value={CharacterFactory.npc}>{CharacterFactory.npc.label}</option>
    </select>

    <input type="submit" value="Create Character" />
  </form>

  {#each Object.keys($characters).reverse() as key}
    <CharacterCard
      name={$characters[key].name}
      inventory={$characters[key].inventory}
      incantations={$characters[key].incantations}
      characterClass={$characters[key].characterClass}
      inventoryLoadingMessage={$characters[key].inventoryLoadingMessage}
    />
  {/each}
</div>

<style>
  .inputfield {
    display: block;
    width: 100%;
  }
</style>
