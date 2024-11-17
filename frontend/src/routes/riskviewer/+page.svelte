<script lang="ts">
	import RiskDossierHeader from '$lib/components/RiskDossierHeader.svelte';
	import { columns } from './columns.js';
	import DataTable from './data-table.svelte';

	let { data } = $props();
	const tableData = $derived(data);
</script>

<RiskDossierHeader></RiskDossierHeader>
<br />
<DataTable data={tableData.data} {columns} />
