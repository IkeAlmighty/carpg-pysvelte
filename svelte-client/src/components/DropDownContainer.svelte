<script>
  let isVisible = true;

  export let child;
  export let panelName = "";

  function toggle() {
    isVisible = !isVisible;
  }
</script>

<div class="container">
  <div>
    <button class="dropdown-button" on:click={toggle}>
      {isVisible ? "Hide " : "Show "}{panelName}
    </button>
  </div>

  {#if isVisible}
    <div><svelte:component this={child} /></div>
  {/if}
</div>

<style>
  .dropdown-button {
    width: 100%;
  }

  .container {
    width: 100%;
  }
</style>
