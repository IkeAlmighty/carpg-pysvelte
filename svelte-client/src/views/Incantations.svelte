<script>
  import { onMount } from "svelte";
  import { fetchTranslation } from "../utilities/endpoints";

  let spell = undefined;
  let text = undefined;
  let seed = "playtest";

  const getTranslation = (e) => {
    e.preventDefault();
    if (seed === undefined || text === undefined) {
      console.log(spell, text, seed);
      return;
    }
    fetchTranslation(text, seed)
      .then((res) => {
        spell = res.data;
      })
      .catch((error) => {});
  };
</script>

<div class="container">
  <h1>Incantation Translator</h1>
  <div class="d-block">
    <form on:submit={getTranslation}>
      <input type="text" bind:value={seed} placeholder="language seed" />
      <input type="text" bind:value={text} placeholder="translate..." />
      <input type="submit" value="translate" />
    </form>
  </div>

  <div class="d-block">
    {#if spell}
      {spell[0]}
    {/if}
  </div>
</div>

<style>
  .d-block {
    display: block;
    margin: 10px 0;
  }

  input {
    width: 100%;
  }
</style>
