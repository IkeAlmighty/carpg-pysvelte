<script>
  import { onMount } from "svelte";

  export let item;
  let isWeapon = false;
  let isRanged = false;

  //TODO: this table probably should not be hardcoded? idk
  let tierDmgTable = {
    error: "!entry error!",
    5: "1d6 - 2",
    4: "1d6 - 1",
    3: "1d6 + 2",
    2: "1d6 + 6",
    1: "2d6 + 6",
  };

  const getDamage = (item) => {
    let tier = parseInt(item[3]);
    if (isNaN(tier)) tier = "error";
    return tierDmgTable[tier];
  };

  onMount(() => {
    let tags = item[4].split(",").map((item) => item.trim().toUpperCase());
    isWeapon = tags.includes("WEAPON");
    isRanged = tags.includes("RANGED");
  });
</script>

<div class="my-1 item-container">
  <strong>{item[0]}</strong>
  <div class="d-block text-small italic">
    {#if isWeapon}
      Deals {getDamage(item)}
      {#if isRanged}ranged{/if} damage in combat.
    {/if}
  </div>
  <div class="d-block text-small">
    {#if item[1].trim() != "-"}
      Description/Action: {item[1]}
    {/if}
  </div>
  <div class="d-block text-small">
    {#if item[2].trim() != "-"}
      {item[2]} lbs
    {/if}
  </div>
  <div class="d-block text-small">
    {#if item[5]}
      <strong>Spell:</strong> {item[5][0]}
    {/if}
  </div>
</div>

<style>
  .item-container {
    margin: 20px 0;
  }
</style>
