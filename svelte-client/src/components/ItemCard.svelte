<script>
  export let item;
</script>

<div class="my-1 item-container">
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
</div>

<style>
  .item-container {
    max-width: 300px;
  }
</style>
