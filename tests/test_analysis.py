# tests/test_analysis.py

from src.analysis import run_analysis

def test_run_analysis():
    results = run_analysis()
    
    # Assert that the analysis results contain 'mean' and 'sum'
    assert 'mean' in results
    assert 'sum' in results
    
    # You can also test for expected values based on the dataset
    assert results['mean'] == 30.0
    assert results['sum'] == 150

